# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import search_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.company_basic import CompanyBasic

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_models: List[str] | NotGiven = NOT_GIVEN,
        employees_change: Iterable[float] | NotGiven = NOT_GIVEN,
        employees_change_time: Literal["month", "quarter", "six_month", "annual"] | NotGiven = NOT_GIVEN,
        employees_on_professional_networks_range: Iterable[int] | NotGiven = NOT_GIVEN,
        end_customer: List[str] | NotGiven = NOT_GIVEN,
        funding_size: Iterable[int] | NotGiven = NOT_GIVEN,
        funding_stage: List[str] | NotGiven = NOT_GIVEN,
        grata_employees_estimates_range: Iterable[int] | NotGiven = NOT_GIVEN,
        headquarters: search_create_params.Headquarters | NotGiven = NOT_GIVEN,
        industry_classifications: search_create_params.IndustryClassifications | NotGiven = NOT_GIVEN,
        is_funded: bool | NotGiven = NOT_GIVEN,
        lists: search_create_params.Lists | NotGiven = NOT_GIVEN,
        ownership: List[str] | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        terms_exclude: List[str] | NotGiven = NOT_GIVEN,
        terms_include: search_create_params.TermsInclude | NotGiven = NOT_GIVEN,
        year_founded: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyBasic:
        """Returns Grata-powered search results based on an input search query.

        If you're
        using any of the filters in the UI that are not presented below, the results may
        differ.

        Args:
          page_token: Page token used for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1.4/search/",
            body=maybe_transform(
                {
                    "business_models": business_models,
                    "employees_change": employees_change,
                    "employees_change_time": employees_change_time,
                    "employees_on_professional_networks_range": employees_on_professional_networks_range,
                    "end_customer": end_customer,
                    "funding_size": funding_size,
                    "funding_stage": funding_stage,
                    "grata_employees_estimates_range": grata_employees_estimates_range,
                    "headquarters": headquarters,
                    "industry_classifications": industry_classifications,
                    "is_funded": is_funded,
                    "lists": lists,
                    "ownership": ownership,
                    "page_token": page_token,
                    "terms_exclude": terms_exclude,
                    "terms_include": terms_include,
                    "year_founded": year_founded,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyBasic,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_models: List[str] | NotGiven = NOT_GIVEN,
        employees_change: Iterable[float] | NotGiven = NOT_GIVEN,
        employees_change_time: Literal["month", "quarter", "six_month", "annual"] | NotGiven = NOT_GIVEN,
        employees_on_professional_networks_range: Iterable[int] | NotGiven = NOT_GIVEN,
        end_customer: List[str] | NotGiven = NOT_GIVEN,
        funding_size: Iterable[int] | NotGiven = NOT_GIVEN,
        funding_stage: List[str] | NotGiven = NOT_GIVEN,
        grata_employees_estimates_range: Iterable[int] | NotGiven = NOT_GIVEN,
        headquarters: search_create_params.Headquarters | NotGiven = NOT_GIVEN,
        industry_classifications: search_create_params.IndustryClassifications | NotGiven = NOT_GIVEN,
        is_funded: bool | NotGiven = NOT_GIVEN,
        lists: search_create_params.Lists | NotGiven = NOT_GIVEN,
        ownership: List[str] | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        terms_exclude: List[str] | NotGiven = NOT_GIVEN,
        terms_include: search_create_params.TermsInclude | NotGiven = NOT_GIVEN,
        year_founded: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyBasic:
        """Returns Grata-powered search results based on an input search query.

        If you're
        using any of the filters in the UI that are not presented below, the results may
        differ.

        Args:
          page_token: Page token used for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1.4/search/",
            body=await async_maybe_transform(
                {
                    "business_models": business_models,
                    "employees_change": employees_change,
                    "employees_change_time": employees_change_time,
                    "employees_on_professional_networks_range": employees_on_professional_networks_range,
                    "end_customer": end_customer,
                    "funding_size": funding_size,
                    "funding_stage": funding_stage,
                    "grata_employees_estimates_range": grata_employees_estimates_range,
                    "headquarters": headquarters,
                    "industry_classifications": industry_classifications,
                    "is_funded": is_funded,
                    "lists": lists,
                    "ownership": ownership,
                    "page_token": page_token,
                    "terms_exclude": terms_exclude,
                    "terms_include": terms_include,
                    "year_founded": year_founded,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyBasic,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_raw_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_raw_response_wrapper(
            search.create,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.create = to_streamed_response_wrapper(
            search.create,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.create = async_to_streamed_response_wrapper(
            search.create,
        )
