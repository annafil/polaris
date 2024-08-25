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
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CatalogPrivilege(str, Enum):
    """
    CatalogPrivilege
    """

    """
    allowed enum values
    """
    CATALOG_MANAGE_ACCESS = 'CATALOG_MANAGE_ACCESS'
    CATALOG_MANAGE_CONTENT = 'CATALOG_MANAGE_CONTENT'
    CATALOG_MANAGE_METADATA = 'CATALOG_MANAGE_METADATA'
    CATALOG_READ_PROPERTIES = 'CATALOG_READ_PROPERTIES'
    CATALOG_WRITE_PROPERTIES = 'CATALOG_WRITE_PROPERTIES'
    NAMESPACE_CREATE = 'NAMESPACE_CREATE'
    TABLE_CREATE = 'TABLE_CREATE'
    VIEW_CREATE = 'VIEW_CREATE'
    NAMESPACE_DROP = 'NAMESPACE_DROP'
    TABLE_DROP = 'TABLE_DROP'
    VIEW_DROP = 'VIEW_DROP'
    NAMESPACE_LIST = 'NAMESPACE_LIST'
    TABLE_LIST = 'TABLE_LIST'
    VIEW_LIST = 'VIEW_LIST'
    NAMESPACE_READ_PROPERTIES = 'NAMESPACE_READ_PROPERTIES'
    TABLE_READ_PROPERTIES = 'TABLE_READ_PROPERTIES'
    VIEW_READ_PROPERTIES = 'VIEW_READ_PROPERTIES'
    NAMESPACE_WRITE_PROPERTIES = 'NAMESPACE_WRITE_PROPERTIES'
    TABLE_WRITE_PROPERTIES = 'TABLE_WRITE_PROPERTIES'
    VIEW_WRITE_PROPERTIES = 'VIEW_WRITE_PROPERTIES'
    TABLE_READ_DATA = 'TABLE_READ_DATA'
    TABLE_WRITE_DATA = 'TABLE_WRITE_DATA'
    NAMESPACE_FULL_METADATA = 'NAMESPACE_FULL_METADATA'
    TABLE_FULL_METADATA = 'TABLE_FULL_METADATA'
    VIEW_FULL_METADATA = 'VIEW_FULL_METADATA'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CatalogPrivilege from a JSON string"""
        return cls(json.loads(json_str))


