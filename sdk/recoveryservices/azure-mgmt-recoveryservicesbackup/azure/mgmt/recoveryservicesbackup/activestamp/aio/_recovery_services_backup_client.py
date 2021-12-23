# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import RecoveryServicesBackupClientConfiguration
from .operations import BMSPrepareDataMoveOperationResultOperations, BackupEnginesOperations, BackupJobsOperations, BackupOperationResultsOperations, BackupOperationStatusesOperations, BackupPoliciesOperations, BackupProtectableItemsOperations, BackupProtectedItemsOperations, BackupProtectionContainersOperations, BackupProtectionIntentOperations, BackupResourceEncryptionConfigsOperations, BackupResourceStorageConfigsNonCRROperations, BackupResourceVaultConfigsOperations, BackupStatusOperations, BackupUsageSummariesOperations, BackupWorkloadItemsOperations, BackupsOperations, ExportJobsOperationResultsOperations, FeatureSupportOperations, ItemLevelRecoveryConnectionsOperations, JobCancellationsOperations, JobDetailsOperations, JobOperationResultsOperations, JobsOperations, OperationOperations, Operations, PrivateEndpointConnectionOperations, PrivateEndpointOperations, ProtectableContainersOperations, ProtectedItemOperationResultsOperations, ProtectedItemOperationStatusesOperations, ProtectedItemsOperations, ProtectionContainerOperationResultsOperations, ProtectionContainerRefreshOperationResultsOperations, ProtectionContainersOperations, ProtectionIntentOperations, ProtectionPoliciesOperations, ProtectionPolicyOperationResultsOperations, ProtectionPolicyOperationStatusesOperations, RecoveryPointsOperations, RecoveryPointsRecommendedForMoveOperations, RecoveryServicesBackupClientOperationsMixin, ResourceGuardProxiesOperations, ResourceGuardProxyOperations, RestoresOperations, SecurityPINsOperations, ValidateOperationOperations, ValidateOperationResultsOperations, ValidateOperationStatusesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class RecoveryServicesBackupClient(RecoveryServicesBackupClientOperationsMixin):
    """Open API 2.0 Specs for Azure RecoveryServices Backup service.

    :ivar backup_resource_storage_configs_non_crr: BackupResourceStorageConfigsNonCRROperations
     operations
    :vartype backup_resource_storage_configs_non_crr:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupResourceStorageConfigsNonCRROperations
    :ivar protection_intent: ProtectionIntentOperations operations
    :vartype protection_intent:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionIntentOperations
    :ivar backup_status: BackupStatusOperations operations
    :vartype backup_status:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupStatusOperations
    :ivar feature_support: FeatureSupportOperations operations
    :vartype feature_support:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.FeatureSupportOperations
    :ivar backup_protection_intent: BackupProtectionIntentOperations operations
    :vartype backup_protection_intent:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupProtectionIntentOperations
    :ivar backup_usage_summaries: BackupUsageSummariesOperations operations
    :vartype backup_usage_summaries:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupUsageSummariesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.Operations
    :ivar backup_resource_vault_configs: BackupResourceVaultConfigsOperations operations
    :vartype backup_resource_vault_configs:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupResourceVaultConfigsOperations
    :ivar backup_resource_encryption_configs: BackupResourceEncryptionConfigsOperations operations
    :vartype backup_resource_encryption_configs:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupResourceEncryptionConfigsOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.PrivateEndpointConnectionOperations
    :ivar private_endpoint: PrivateEndpointOperations operations
    :vartype private_endpoint:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.PrivateEndpointOperations
    :ivar bms_prepare_data_move_operation_result: BMSPrepareDataMoveOperationResultOperations
     operations
    :vartype bms_prepare_data_move_operation_result:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BMSPrepareDataMoveOperationResultOperations
    :ivar protected_items: ProtectedItemsOperations operations
    :vartype protected_items:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectedItemsOperations
    :ivar protected_item_operation_results: ProtectedItemOperationResultsOperations operations
    :vartype protected_item_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectedItemOperationResultsOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.RecoveryPointsOperations
    :ivar restores: RestoresOperations operations
    :vartype restores:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.RestoresOperations
    :ivar backup_policies: BackupPoliciesOperations operations
    :vartype backup_policies:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupPoliciesOperations
    :ivar protection_policies: ProtectionPoliciesOperations operations
    :vartype protection_policies:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionPoliciesOperations
    :ivar protection_policy_operation_results: ProtectionPolicyOperationResultsOperations
     operations
    :vartype protection_policy_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionPolicyOperationResultsOperations
    :ivar backup_jobs: BackupJobsOperations operations
    :vartype backup_jobs:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupJobsOperations
    :ivar job_details: JobDetailsOperations operations
    :vartype job_details:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.JobDetailsOperations
    :ivar job_cancellations: JobCancellationsOperations operations
    :vartype job_cancellations:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.JobCancellationsOperations
    :ivar job_operation_results: JobOperationResultsOperations operations
    :vartype job_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.JobOperationResultsOperations
    :ivar export_jobs_operation_results: ExportJobsOperationResultsOperations operations
    :vartype export_jobs_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ExportJobsOperationResultsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.JobsOperations
    :ivar backup_protected_items: BackupProtectedItemsOperations operations
    :vartype backup_protected_items:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupProtectedItemsOperations
    :ivar operation: OperationOperations operations
    :vartype operation:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.OperationOperations
    :ivar validate_operation: ValidateOperationOperations operations
    :vartype validate_operation:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ValidateOperationOperations
    :ivar validate_operation_results: ValidateOperationResultsOperations operations
    :vartype validate_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ValidateOperationResultsOperations
    :ivar validate_operation_statuses: ValidateOperationStatusesOperations operations
    :vartype validate_operation_statuses:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ValidateOperationStatusesOperations
    :ivar backup_engines: BackupEnginesOperations operations
    :vartype backup_engines:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupEnginesOperations
    :ivar protection_container_refresh_operation_results:
     ProtectionContainerRefreshOperationResultsOperations operations
    :vartype protection_container_refresh_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionContainerRefreshOperationResultsOperations
    :ivar protectable_containers: ProtectableContainersOperations operations
    :vartype protectable_containers:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectableContainersOperations
    :ivar protection_containers: ProtectionContainersOperations operations
    :vartype protection_containers:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionContainersOperations
    :ivar backup_workload_items: BackupWorkloadItemsOperations operations
    :vartype backup_workload_items:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupWorkloadItemsOperations
    :ivar protection_container_operation_results: ProtectionContainerOperationResultsOperations
     operations
    :vartype protection_container_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionContainerOperationResultsOperations
    :ivar backups: BackupsOperations operations
    :vartype backups:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupsOperations
    :ivar protected_item_operation_statuses: ProtectedItemOperationStatusesOperations operations
    :vartype protected_item_operation_statuses:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectedItemOperationStatusesOperations
    :ivar item_level_recovery_connections: ItemLevelRecoveryConnectionsOperations operations
    :vartype item_level_recovery_connections:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ItemLevelRecoveryConnectionsOperations
    :ivar backup_operation_results: BackupOperationResultsOperations operations
    :vartype backup_operation_results:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupOperationResultsOperations
    :ivar backup_operation_statuses: BackupOperationStatusesOperations operations
    :vartype backup_operation_statuses:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupOperationStatusesOperations
    :ivar protection_policy_operation_statuses: ProtectionPolicyOperationStatusesOperations
     operations
    :vartype protection_policy_operation_statuses:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ProtectionPolicyOperationStatusesOperations
    :ivar backup_protectable_items: BackupProtectableItemsOperations operations
    :vartype backup_protectable_items:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupProtectableItemsOperations
    :ivar backup_protection_containers: BackupProtectionContainersOperations operations
    :vartype backup_protection_containers:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.BackupProtectionContainersOperations
    :ivar security_pins: SecurityPINsOperations operations
    :vartype security_pins:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.SecurityPINsOperations
    :ivar recovery_points_recommended_for_move: RecoveryPointsRecommendedForMoveOperations
     operations
    :vartype recovery_points_recommended_for_move:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.RecoveryPointsRecommendedForMoveOperations
    :ivar resource_guard_proxies: ResourceGuardProxiesOperations operations
    :vartype resource_guard_proxies:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ResourceGuardProxiesOperations
    :ivar resource_guard_proxy: ResourceGuardProxyOperations operations
    :vartype resource_guard_proxy:
     azure.mgmt.recoveryservicesbackup.activestamp.aio.operations.ResourceGuardProxyOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = RecoveryServicesBackupClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.backup_resource_storage_configs_non_crr = BackupResourceStorageConfigsNonCRROperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_intent = ProtectionIntentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_status = BackupStatusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.feature_support = FeatureSupportOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_protection_intent = BackupProtectionIntentOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_usage_summaries = BackupUsageSummariesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_resource_vault_configs = BackupResourceVaultConfigsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_resource_encryption_configs = BackupResourceEncryptionConfigsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint = PrivateEndpointOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bms_prepare_data_move_operation_result = BMSPrepareDataMoveOperationResultOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protected_items = ProtectedItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protected_item_operation_results = ProtectedItemOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.recovery_points = RecoveryPointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.restores = RestoresOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_policies = BackupPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_policies = ProtectionPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_policy_operation_results = ProtectionPolicyOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_jobs = BackupJobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_details = JobDetailsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_cancellations = JobCancellationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.job_operation_results = JobOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.export_jobs_operation_results = ExportJobsOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_protected_items = BackupProtectedItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.validate_operation = ValidateOperationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.validate_operation_results = ValidateOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.validate_operation_statuses = ValidateOperationStatusesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_engines = BackupEnginesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_container_refresh_operation_results = ProtectionContainerRefreshOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protectable_containers = ProtectableContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_containers = ProtectionContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_workload_items = BackupWorkloadItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_container_operation_results = ProtectionContainerOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backups = BackupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protected_item_operation_statuses = ProtectedItemOperationStatusesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.item_level_recovery_connections = ItemLevelRecoveryConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_operation_results = BackupOperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_operation_statuses = BackupOperationStatusesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.protection_policy_operation_statuses = ProtectionPolicyOperationStatusesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_protectable_items = BackupProtectableItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_protection_containers = BackupProtectionContainersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.security_pins = SecurityPINsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.recovery_points_recommended_for_move = RecoveryPointsRecommendedForMoveOperations(self._client, self._config, self._serialize, self._deserialize)
        self.resource_guard_proxies = ResourceGuardProxiesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.resource_guard_proxy = ResourceGuardProxyOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "RecoveryServicesBackupClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
