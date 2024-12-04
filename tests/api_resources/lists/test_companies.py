# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from grata import Grata, AsyncGrata
from tests.utils import assert_matches_type
from grata.types.lists import ListModifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompanies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_modify(self, client: Grata) -> None:
        company = client.lists.companies.modify(
            list_uid="XYZ12345",
        )
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    def test_method_modify_with_all_params(self, client: Grata) -> None:
        company = client.lists.companies.modify(
            list_uid="XYZ12345",
            action="add",
            domains=["grata.com"],
            uids=["XYZ12356"],
        )
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    def test_raw_response_modify(self, client: Grata) -> None:
        response = client.lists.companies.with_raw_response.modify(
            list_uid="XYZ12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    def test_streaming_response_modify(self, client: Grata) -> None:
        with client.lists.companies.with_streaming_response.modify(
            list_uid="XYZ12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = response.parse()
            assert_matches_type(ListModifyResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_modify(self, client: Grata) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_uid` but received ''"):
            client.lists.companies.with_raw_response.modify(
                list_uid="",
            )


class TestAsyncCompanies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_modify(self, async_client: AsyncGrata) -> None:
        company = await async_client.lists.companies.modify(
            list_uid="XYZ12345",
        )
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    async def test_method_modify_with_all_params(self, async_client: AsyncGrata) -> None:
        company = await async_client.lists.companies.modify(
            list_uid="XYZ12345",
            action="add",
            domains=["grata.com"],
            uids=["XYZ12356"],
        )
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    async def test_raw_response_modify(self, async_client: AsyncGrata) -> None:
        response = await async_client.lists.companies.with_raw_response.modify(
            list_uid="XYZ12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = await response.parse()
        assert_matches_type(ListModifyResponse, company, path=["response"])

    @parametrize
    async def test_streaming_response_modify(self, async_client: AsyncGrata) -> None:
        async with async_client.lists.companies.with_streaming_response.modify(
            list_uid="XYZ12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            company = await response.parse()
            assert_matches_type(ListModifyResponse, company, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_modify(self, async_client: AsyncGrata) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_uid` but received ''"):
            await async_client.lists.companies.with_raw_response.modify(
                list_uid="",
            )
