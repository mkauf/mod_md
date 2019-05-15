/* Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef mod_md_md_status_h
#define mod_md_md_status_h

struct md_reg_t;

typedef struct {
    const md_t *md;

    int stalled;
    int renewed;
    int renewal_notified;
    apr_time_t restart_at;
    int need_restart;
    int restart_processed;

    apr_status_t last_rv;
    apr_time_t next_check;
    int error_runs;
} md_job_t;

apr_status_t md_job_update(struct md_reg_t *reg, md_job_t *job, apr_pool_t *p);


int md_http_cert_status(request_rec *r);

int md_status_hook(request_rec *r, int flags);

#endif /* mod_md_md_status_h */