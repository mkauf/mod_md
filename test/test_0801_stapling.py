# test mod_md stapling support

import json
import os
import pytest
import re
import socket
import ssl
import sys
import time

from datetime import datetime
from httplib import HTTPSConnection
from test_base import TestEnv
from test_base import HttpdConf
from test_base import CertUtil


def setup_module(module):
    print("setup_module    module:%s" % module.__name__)
    TestEnv.init()
    TestEnv.APACHE_CONF_SRC = "data/test_auto"
    TestEnv.check_acme()
    TestEnv.clear_store()
    TestEnv.install_test_conf();
    assert TestEnv.apache_start() == 0
    

def teardown_module(module):
    print("teardown_module module:%s" % module.__name__)
    assert TestEnv.apache_stop() == 0


class TestStapling:

    def setup_method(self, method):
        print("setup_method: %s" % method.__name__)
        TestEnv.apache_err_reset();
        TestEnv.clear_store()
        self.test_domain = TestEnv.get_method_domain(method)

    def teardown_method(self, method):
        print("teardown_method: %s" % method.__name__)

    #-----------------------------------------------------------------------------------------------
    # MD with stapling enabled, mod_ssl stapling off
    def test_801_001(self):
        domain = self.test_domain
        dns_list = [ domain ]
        # Start with default stapling (off), check that none is reported/used on connections
        conf = HttpdConf()
        conf.add_admin( "admin@" + domain )
        conf.add_md( dns_list )
        conf.add_vhost( TestEnv.HTTPS_PORT, domain, aliasList=[])
        conf.install()
        assert TestEnv.apache_restart() == 0
        assert TestEnv.await_completion( [ domain ] )
        assert TestEnv.apache_restart() == 0
        TestEnv.check_md_complete(domain)
        stat = TestEnv.get_ocsp_status(domain)
        assert stat['ocsp'] == "no response sent" 
        stat = TestEnv.get_md_status(domain)
        assert not stat["stapling"]
        #
        # turn stapling on, wait for it to appear in connections
        conf = HttpdConf()
        conf.add_admin( "admin@" + domain )
        conf.add_line("MDStapling on")
        conf.add_md( dns_list )
        conf.add_vhost( TestEnv.HTTPS_PORT, domain, aliasList=[])
        conf.install()
        assert TestEnv.apache_restart() == 0
        stat = TestEnv.await_ocsp_status(domain)
        assert stat['ocsp'] == "successful (0x0)" 
        assert stat['verify'] == "0 (ok)"
        stat = TestEnv.get_md_status(domain)
        assert stat["stapling"]
        assert stat["ocsp"]["status"] == "good"
        assert stat["ocsp"]["valid"]
        #
        # turn stapling off (explicitly) again, should disappear
        conf = HttpdConf()
        conf.add_admin( "admin@" + domain )
        conf.add_line("MDStapling off")
        conf.add_md( dns_list )
        conf.add_vhost( TestEnv.HTTPS_PORT, domain, aliasList=[])
        conf.install()
        assert TestEnv.apache_restart() == 0
        stat = TestEnv.get_ocsp_status(domain)
        assert stat['ocsp'] == "no response sent" 
        stat = TestEnv.get_md_status(domain)
        assert not stat["stapling"]
        


