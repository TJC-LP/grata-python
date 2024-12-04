# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.lists import company_modify_params
from ..._base_client import make_request_options
from ...types.lists.list_modify_response import ListModifyResponse

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def modify(
        self,
        list_uid: str,
        *,
        action: Literal["add", "remove"] | NotGiven = NOT_GIVEN,
        domains: List[str] | NotGiven = NOT_GIVEN,
        uids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListModifyResponse:
        """
        The modify call will allow users to add or remove companies from an existing
        list. Private lists are not eligible to be updated with this call.

        Args:
          action: Action to perform on the list.

          domains: Domains to add or remove from a list (max of 500 permitted per call).

          uids: Grata company UIDs to add or remove from a list (max of 500 permitted per call).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return self._post(
            f"/api/v1.4/lists/{list_uid}/companies/",
            body=maybe_transform(
                {
                    "action": action,
                    "domains": domains,
                    "uids": uids,
                },
                company_modify_params.CompanyModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListModifyResponse,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def modify(
        self,
        list_uid: str,
        *,
        action: Literal["add", "remove"] | NotGiven = NOT_GIVEN,
        domains: List[str] | NotGiven = NOT_GIVEN,
        uids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListModifyResponse:
        """
        The modify call will allow users to add or remove companies from an existing
        list. Private lists are not eligible to be updated with this call.

        Args:
          action: Action to perform on the list.

          domains: Domains to add or remove from a list (max of 500 permitted per call).

          uids: Grata company UIDs to add or remove from a list (max of 500 permitted per call).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return await self._post(
            f"/api/v1.4/lists/{list_uid}/companies/",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "domains": domains,
                    "uids": uids,
                },
                company_modify_params.CompanyModifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListModifyResponse,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.modify = to_raw_response_wrapper(
            companies.modify,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.modify = async_to_raw_response_wrapper(
            companies.modify,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.modify = to_streamed_response_wrapper(
            companies.modify,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.modify = async_to_streamed_response_wrapper(
            companies.modify,
        )
