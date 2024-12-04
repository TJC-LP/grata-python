# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import list_list_params, list_create_params, list_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.list_response import ListResponse
from ...types.list_search_response import ListSearchResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """The create call will allow users to create a list in Grata.

        The list visibility
        will be set to organization and it will be visible in the Grata UI for all users
        within the account to view.

        Args:
          name: Name of list being created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1.4/lists/",
            body=maybe_transform({"name": name}, list_create_params.ListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    def retrieve(
        self,
        list_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """
        Grata's List Details API returns key data points about a list, including the
        UID, created date, last updated date, and count of companies in the list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return self._get(
            f"/api/v1.4/lists/{list_uid}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    def update(
        self,
        list_uid: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """Grata's Update List Name API enables you to update the name of a list.

        Private
        lists are not eligible to be updated with this call.

        Args:
          name: New list name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return self._patch(
            f"/api/v1.4/lists/{list_uid}/",
            body=maybe_transform({"name": name}, list_update_params.ListUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListSearchResponse:
        """
        Grata's Search Lists API enables you to search for and return details about the
        lists in your organization. Private lists will not be returned with this call.

        Args:
          name: List name

          page: The page of results to be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1.4/lists/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                    },
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListSearchResponse,
        )

    def delete(
        self,
        list_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Grata's Delete List API enables you to delete an existing list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1.4/lists/{list_uid}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncListsResource(AsyncAPIResource):
    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TJC-LP/grata-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TJC-LP/grata-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """The create call will allow users to create a list in Grata.

        The list visibility
        will be set to organization and it will be visible in the Grata UI for all users
        within the account to view.

        Args:
          name: Name of list being created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1.4/lists/",
            body=await async_maybe_transform({"name": name}, list_create_params.ListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    async def retrieve(
        self,
        list_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """
        Grata's List Details API returns key data points about a list, including the
        UID, created date, last updated date, and count of companies in the list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return await self._get(
            f"/api/v1.4/lists/{list_uid}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    async def update(
        self,
        list_uid: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListResponse:
        """Grata's Update List Name API enables you to update the name of a list.

        Private
        lists are not eligible to be updated with this call.

        Args:
          name: New list name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        return await self._patch(
            f"/api/v1.4/lists/{list_uid}/",
            body=await async_maybe_transform({"name": name}, list_update_params.ListUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListResponse,
        )

    async def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListSearchResponse:
        """
        Grata's Search Lists API enables you to search for and return details about the
        lists in your organization. Private lists will not be returned with this call.

        Args:
          name: List name

          page: The page of results to be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1.4/lists/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                    },
                    list_list_params.ListListParams,
                ),
            ),
            cast_to=ListSearchResponse,
        )

    async def delete(
        self,
        list_uid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Grata's Delete List API enables you to delete an existing list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not list_uid:
            raise ValueError(f"Expected a non-empty value for `list_uid` but received {list_uid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1.4/lists/{list_uid}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_raw_response_wrapper(
            lists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            lists.retrieve,
        )
        self.update = to_raw_response_wrapper(
            lists.update,
        )
        self.list = to_raw_response_wrapper(
            lists.list,
        )
        self.delete = to_raw_response_wrapper(
            lists.delete,
        )

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._lists.companies)


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_raw_response_wrapper(
            lists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            lists.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            lists.update,
        )
        self.list = async_to_raw_response_wrapper(
            lists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lists.delete,
        )

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._lists.companies)


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.create = to_streamed_response_wrapper(
            lists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            lists.update,
        )
        self.list = to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = to_streamed_response_wrapper(
            lists.delete,
        )

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._lists.companies)


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.create = async_to_streamed_response_wrapper(
            lists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            lists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lists.delete,
        )

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._lists.companies)
