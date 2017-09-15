/* Copyright 2015 greenbytes GmbH (https://www.greenbytes.de)
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0

* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#ifndef mod_md_md_version_h
#define mod_md_md_version_h

#undef PACKAGE_VERSION
#undef PACKAGE_TARNAME
#undef PACKAGE_STRING
#undef PACKAGE_NAME
#undef PACKAGE_BUGREPORT

/**
 * @macro
 * Version number of the md module as c string
 */
#define MOD_MD_VERSION "0.9.6-git"

/**
 * @macro
 * Numerical representation of the version number of the md module
 * release. This is a 24 bit number with 8 bits for major number, 8 bits
 * for minor and 8 bits for patch. Version 1.2.3 becomes 0x010203.
 */
#define MOD_MD_VERSION_NUM 0x000906

#define MD_EXPERIMENTAL 0
#define MD_ACME_DEF_URL    "https://acme-v01.api.letsencrypt.org/directory"

#endif /* mod_md_md_version_h */
