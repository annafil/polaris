#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# coding: utf-8

"""
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.catalog.models.assert_default_sort_order_id import AssertDefaultSortOrderId

class TestAssertDefaultSortOrderId(unittest.TestCase):
    """AssertDefaultSortOrderId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssertDefaultSortOrderId:
        """Test AssertDefaultSortOrderId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssertDefaultSortOrderId`
        """
        model = AssertDefaultSortOrderId()
        if include_optional:
            return AssertDefaultSortOrderId(
                type = 'assert-default-sort-order-id',
                default_sort_order_id = 56
            )
        else:
            return AssertDefaultSortOrderId(
                type = 'assert-default-sort-order-id',
                default_sort_order_id = 56,
        )
        """

    def testAssertDefaultSortOrderId(self):
        """Test AssertDefaultSortOrderId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
