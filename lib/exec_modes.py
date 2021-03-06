# Copyright 2016 The Jackson Laboratory
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import job_runner.common


class ToolExecModes(object):
    NO_SUB = 0
    BATCH_STANDARD = 1
    BATCH_MANAGED = 2
    CLOUD_GCP = 3

    _strings = {
        BATCH_STANDARD: "Standard Batch",
        BATCH_MANAGED: "Managed Batch",
        CLOUD_GCP: "Google Cloud Platform"
    }

    def __init__(self):
        raise Exception("Do not instantiate the ToolExecModes class. "
                        "It is an enumeration")

    @staticmethod
    def to_str(mode):
        return ToolExecModes._strings[mode]

    @staticmethod
    def get_exec_mode(log_dir):
        if os.path.exists(os.path.join(log_dir,
                                       job_runner.common.MANAGED_MODE_FLAG)):
            return ToolExecModes.BATCH_MANAGED
        elif os.path.exists(os.path.join(log_dir,
                                         job_runner.common.GCP_MODE_FLAG)):
            return ToolExecModes.CLOUD_GCP
        elif os.path.exists(os.path.join(log_dir,
                                         job_runner.common.NO_SUB_FLAG)):
            return ToolExecModes.NO_SUB
        return ToolExecModes.BATCH_STANDARD
