# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._balances_operations import build_get_by_billing_account_request, build_get_for_billing_period_by_billing_account_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BalancesOperations:
    """BalancesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.consumption.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_by_billing_account(
        self,
        billing_account_id: str,
        **kwargs: Any
    ) -> "_models.Balance":
        """Gets the balances for a scope by billingAccountId. Balances are available via this API only for
        May 1, 2014 or later.

        :param billing_account_id: BillingAccount ID.
        :type billing_account_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Balance, or the result of cls(response)
        :rtype: ~azure.mgmt.consumption.models.Balance
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Balance"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_by_billing_account_request(
            billing_account_id=billing_account_id,
            template_url=self.get_by_billing_account.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Balance', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/balances'}  # type: ignore


    @distributed_trace_async
    async def get_for_billing_period_by_billing_account(
        self,
        billing_account_id: str,
        billing_period_name: str,
        **kwargs: Any
    ) -> "_models.Balance":
        """Gets the balances for a scope by billing period and billingAccountId. Balances are available
        via this API only for May 1, 2014 or later.

        :param billing_account_id: BillingAccount ID.
        :type billing_account_id: str
        :param billing_period_name: Billing Period Name.
        :type billing_period_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Balance, or the result of cls(response)
        :rtype: ~azure.mgmt.consumption.models.Balance
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Balance"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_for_billing_period_by_billing_account_request(
            billing_account_id=billing_account_id,
            billing_period_name=billing_period_name,
            template_url=self.get_for_billing_period_by_billing_account.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Balance', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_for_billing_period_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/balances'}  # type: ignore

