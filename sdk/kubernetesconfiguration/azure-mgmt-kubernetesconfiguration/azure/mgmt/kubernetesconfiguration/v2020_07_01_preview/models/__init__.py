# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ComplianceStatus
    from ._models_py3 import ConfigurationIdentity
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExtensionInstance
    from ._models_py3 import ExtensionInstanceUpdate
    from ._models_py3 import ExtensionInstancesList
    from ._models_py3 import ExtensionStatus
    from ._models_py3 import HelmOperatorProperties
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourceProviderOperation
    from ._models_py3 import ResourceProviderOperationDisplay
    from ._models_py3 import ResourceProviderOperationList
    from ._models_py3 import Result
    from ._models_py3 import Scope
    from ._models_py3 import ScopeCluster
    from ._models_py3 import ScopeNamespace
    from ._models_py3 import SourceControlConfiguration
    from ._models_py3 import SourceControlConfigurationList
    from ._models_py3 import SystemData
except (SyntaxError, ImportError):
    from ._models import ComplianceStatus  # type: ignore
    from ._models import ConfigurationIdentity  # type: ignore
    from ._models import ErrorDefinition  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExtensionInstance  # type: ignore
    from ._models import ExtensionInstanceUpdate  # type: ignore
    from ._models import ExtensionInstancesList  # type: ignore
    from ._models import ExtensionStatus  # type: ignore
    from ._models import HelmOperatorProperties  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceProviderOperation  # type: ignore
    from ._models import ResourceProviderOperationDisplay  # type: ignore
    from ._models import ResourceProviderOperationList  # type: ignore
    from ._models import Result  # type: ignore
    from ._models import Scope  # type: ignore
    from ._models import ScopeCluster  # type: ignore
    from ._models import ScopeNamespace  # type: ignore
    from ._models import SourceControlConfiguration  # type: ignore
    from ._models import SourceControlConfigurationList  # type: ignore
    from ._models import SystemData  # type: ignore

from ._source_control_configuration_client_enums import (
    ComplianceStateType,
    Enum0,
    Enum1,
    InstallStateType,
    LevelType,
    MessageLevelType,
    OperatorScopeType,
    OperatorType,
    ProvisioningStateType,
    ResourceIdentityType,
)

__all__ = [
    'ComplianceStatus',
    'ConfigurationIdentity',
    'ErrorDefinition',
    'ErrorResponse',
    'ExtensionInstance',
    'ExtensionInstanceUpdate',
    'ExtensionInstancesList',
    'ExtensionStatus',
    'HelmOperatorProperties',
    'ProxyResource',
    'Resource',
    'ResourceProviderOperation',
    'ResourceProviderOperationDisplay',
    'ResourceProviderOperationList',
    'Result',
    'Scope',
    'ScopeCluster',
    'ScopeNamespace',
    'SourceControlConfiguration',
    'SourceControlConfigurationList',
    'SystemData',
    'ComplianceStateType',
    'Enum0',
    'Enum1',
    'InstallStateType',
    'LevelType',
    'MessageLevelType',
    'OperatorScopeType',
    'OperatorType',
    'ProvisioningStateType',
    'ResourceIdentityType',
]
