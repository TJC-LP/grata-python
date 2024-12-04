# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import bulk_enrichment_create_params
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
from ..types.bulk_company_enrichment import BulkCompanyEnrichment

__all__ = ["BulkEnrichmentResource", "AsyncBulkEnrichmentResource"]


class BulkEnrichmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkEnrichmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return BulkEnrichmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkEnrichmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return BulkEnrichmentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        company_uids: List[str] | NotGiven = NOT_GIVEN,
        domains: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkCompanyEnrichment:
        """
        Provide a set of up to 100 company domains or Grata-specific company IDs to
        return relevant firmographic data on requested companies.

        Args:
          company_uids: An array of unique alphanumeric Grata IDs for the companies.

          domains: An array of domains for the companies being enriched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1.4/bulk/enrich/",
            body=maybe_transform(
                {
                    "company_uids": company_uids,
                    "domains": domains,
                },
                bulk_enrichment_create_params.BulkEnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCompanyEnrichment,
        )


class AsyncBulkEnrichmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkEnrichmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkEnrichmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkEnrichmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncBulkEnrichmentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        company_uids: List[str] | NotGiven = NOT_GIVEN,
        domains: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkCompanyEnrichment:
        """
        Provide a set of up to 100 company domains or Grata-specific company IDs to
        return relevant firmographic data on requested companies.

        Args:
          company_uids: An array of unique alphanumeric Grata IDs for the companies.

          domains: An array of domains for the companies being enriched.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1.4/bulk/enrich/",
            body=await async_maybe_transform(
                {
                    "company_uids": company_uids,
                    "domains": domains,
                },
                bulk_enrichment_create_params.BulkEnrichmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCompanyEnrichment,
        )


class BulkEnrichmentResourceWithRawResponse:
    def __init__(self, bulk_enrichment: BulkEnrichmentResource) -> None:
        self._bulk_enrichment = bulk_enrichment

        self.create = to_raw_response_wrapper(
            bulk_enrichment.create,
        )


class AsyncBulkEnrichmentResourceWithRawResponse:
    def __init__(self, bulk_enrichment: AsyncBulkEnrichmentResource) -> None:
        self._bulk_enrichment = bulk_enrichment

        self.create = async_to_raw_response_wrapper(
            bulk_enrichment.create,
        )


class BulkEnrichmentResourceWithStreamingResponse:
    def __init__(self, bulk_enrichment: BulkEnrichmentResource) -> None:
        self._bulk_enrichment = bulk_enrichment

        self.create = to_streamed_response_wrapper(
            bulk_enrichment.create,
        )


class AsyncBulkEnrichmentResourceWithStreamingResponse:
    def __init__(self, bulk_enrichment: AsyncBulkEnrichmentResource) -> None:
        self._bulk_enrichment = bulk_enrichment

        self.create = async_to_streamed_response_wrapper(
            bulk_enrichment.create,
        )