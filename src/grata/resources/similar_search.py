# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import similar_search_create_params
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
from ..types.similar_company_response import SimilarCompanyResponse

__all__ = ["SimilarSearchResource", "AsyncSimilarSearchResource"]


class SimilarSearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimilarSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return SimilarSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimilarSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return SimilarSearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_models: List[str] | NotGiven = NOT_GIVEN,
        company_uid: str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        employees_change: Iterable[float] | NotGiven = NOT_GIVEN,
        employees_change_time: Literal["month", "quarter", "six_month", "annual"] | NotGiven = NOT_GIVEN,
        employees_on_professional_networks_range: Iterable[int] | NotGiven = NOT_GIVEN,
        end_customer: List[str] | NotGiven = NOT_GIVEN,
        funding_size: Iterable[int] | NotGiven = NOT_GIVEN,
        funding_stage: List[str] | NotGiven = NOT_GIVEN,
        grata_employees_estimates_range: Iterable[int] | NotGiven = NOT_GIVEN,
        headquarters: similar_search_create_params.Headquarters | NotGiven = NOT_GIVEN,
        industry_classifications: similar_search_create_params.IndustryClassifications | NotGiven = NOT_GIVEN,
        is_funded: bool | NotGiven = NOT_GIVEN,
        lists: similar_search_create_params.Lists | NotGiven = NOT_GIVEN,
        ownership: List[str] | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        terms_exclude: List[str] | NotGiven = NOT_GIVEN,
        terms_include: similar_search_create_params.TermsInclude | NotGiven = NOT_GIVEN,
        year_founded: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimilarCompanyResponse:
        """Returns Grata-powered search results based on a similar company search.

        If
        you're using any of the filters in the UI that are not presented below, the
        results may differ.

        Args:
          company_uid: Alphanumeric Grata ID for the company (case-sensitive).

          domain: Domain of the company for similar search. Protocol and path can be included. If
              both the domain and company_uid are specified, domain will be referenced.

          page_token: Page token used for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1.4/search-similar/",
            body=maybe_transform(
                {
                    "business_models": business_models,
                    "company_uid": company_uid,
                    "domain": domain,
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
                similar_search_create_params.SimilarSearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimilarCompanyResponse,
        )


class AsyncSimilarSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimilarSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimilarSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimilarSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncSimilarSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_models: List[str] | NotGiven = NOT_GIVEN,
        company_uid: str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        employees_change: Iterable[float] | NotGiven = NOT_GIVEN,
        employees_change_time: Literal["month", "quarter", "six_month", "annual"] | NotGiven = NOT_GIVEN,
        employees_on_professional_networks_range: Iterable[int] | NotGiven = NOT_GIVEN,
        end_customer: List[str] | NotGiven = NOT_GIVEN,
        funding_size: Iterable[int] | NotGiven = NOT_GIVEN,
        funding_stage: List[str] | NotGiven = NOT_GIVEN,
        grata_employees_estimates_range: Iterable[int] | NotGiven = NOT_GIVEN,
        headquarters: similar_search_create_params.Headquarters | NotGiven = NOT_GIVEN,
        industry_classifications: similar_search_create_params.IndustryClassifications | NotGiven = NOT_GIVEN,
        is_funded: bool | NotGiven = NOT_GIVEN,
        lists: similar_search_create_params.Lists | NotGiven = NOT_GIVEN,
        ownership: List[str] | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        terms_exclude: List[str] | NotGiven = NOT_GIVEN,
        terms_include: similar_search_create_params.TermsInclude | NotGiven = NOT_GIVEN,
        year_founded: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimilarCompanyResponse:
        """Returns Grata-powered search results based on a similar company search.

        If
        you're using any of the filters in the UI that are not presented below, the
        results may differ.

        Args:
          company_uid: Alphanumeric Grata ID for the company (case-sensitive).

          domain: Domain of the company for similar search. Protocol and path can be included. If
              both the domain and company_uid are specified, domain will be referenced.

          page_token: Page token used for pagination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1.4/search-similar/",
            body=await async_maybe_transform(
                {
                    "business_models": business_models,
                    "company_uid": company_uid,
                    "domain": domain,
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
                similar_search_create_params.SimilarSearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimilarCompanyResponse,
        )


class SimilarSearchResourceWithRawResponse:
    def __init__(self, similar_search: SimilarSearchResource) -> None:
        self._similar_search = similar_search

        self.create = to_raw_response_wrapper(
            similar_search.create,
        )


class AsyncSimilarSearchResourceWithRawResponse:
    def __init__(self, similar_search: AsyncSimilarSearchResource) -> None:
        self._similar_search = similar_search

        self.create = async_to_raw_response_wrapper(
            similar_search.create,
        )


class SimilarSearchResourceWithStreamingResponse:
    def __init__(self, similar_search: SimilarSearchResource) -> None:
        self._similar_search = similar_search

        self.create = to_streamed_response_wrapper(
            similar_search.create,
        )


class AsyncSimilarSearchResourceWithStreamingResponse:
    def __init__(self, similar_search: AsyncSimilarSearchResource) -> None:
        self._similar_search = similar_search

        self.create = async_to_streamed_response_wrapper(
            similar_search.create,
        )
