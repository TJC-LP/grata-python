# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import enrichment_create_params
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
from ..types.company_detailed import CompanyDetailed

__all__ = ["EnrichmentResource", "AsyncEnrichmentResource"]


class EnrichmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnrichmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return EnrichmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnrichmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return EnrichmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_uid: str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyDetailed:
        """
        Provide a company domain or Grata-specific company ID to return relevant
        firmographic data on a company.

        Args:
          company_uid: Unique alphanumeric Grata ID for the company (case-sensitive).

          domain: Domain of the company being enriched. Protocol and path can be included. If both
              the domain and company_uid are included, the domain will be referenced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1.4/enrich/",
            body=maybe_transform(
                {
                    "company_uid": company_uid,
                    "domain": domain,
                },
                enrichment_create_params.EnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyDetailed,
        )


class AsyncEnrichmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnrichmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnrichmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnrichmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncEnrichmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_uid: str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompanyDetailed:
        """
        Provide a company domain or Grata-specific company ID to return relevant
        firmographic data on a company.

        Args:
          company_uid: Unique alphanumeric Grata ID for the company (case-sensitive).

          domain: Domain of the company being enriched. Protocol and path can be included. If both
              the domain and company_uid are included, the domain will be referenced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1.4/enrich/",
            body=await async_maybe_transform(
                {
                    "company_uid": company_uid,
                    "domain": domain,
                },
                enrichment_create_params.EnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompanyDetailed,
        )


class EnrichmentResourceWithRawResponse:
    def __init__(self, enrichment: EnrichmentResource) -> None:
        self._enrichment = enrichment

        self.create = to_raw_response_wrapper(
            enrichment.create,
        )


class AsyncEnrichmentResourceWithRawResponse:
    def __init__(self, enrichment: AsyncEnrichmentResource) -> None:
        self._enrichment = enrichment

        self.create = async_to_raw_response_wrapper(
            enrichment.create,
        )


class EnrichmentResourceWithStreamingResponse:
    def __init__(self, enrichment: EnrichmentResource) -> None:
        self._enrichment = enrichment

        self.create = to_streamed_response_wrapper(
            enrichment.create,
        )


class AsyncEnrichmentResourceWithStreamingResponse:
    def __init__(self, enrichment: AsyncEnrichmentResource) -> None:
        self._enrichment = enrichment

        self.create = async_to_streamed_response_wrapper(
            enrichment.create,
        )