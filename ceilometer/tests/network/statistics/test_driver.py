#
# Copyright 2014 NEC Corporation.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ceilometer.network.statistics import driver
from ceilometer.openstack.common import test


class TestDriver(test.BaseTestCase):

    def test_driver_ok(self):

        class OkDriver(driver.Driver):

            def get_sample_data(self, meter_name, resources, cache):
                pass

        OkDriver()

    def test_driver_ng(self):

        class NgDriver(driver.Driver):
            """get_sample_data method is lost."""

        self.assertRaises(TypeError, NgDriver)
