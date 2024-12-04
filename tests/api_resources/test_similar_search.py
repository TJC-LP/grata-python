# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from grata import Grata, AsyncGrata
from grata.types import SimilarCompanyResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimilarSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Grata) -> None:
        similar_search = client.similar_search.create()
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Grata) -> None:
        similar_search = client.similar_search.create(
            business_models=["string"],
            company_uid="26AJRCR2",
            domain="slack.com",
            employees_change=[0],
            employees_change_time="month",
            employees_on_professional_networks_range=[0],
            end_customer=["string"],
            funding_size=[0],
            funding_stage=["string"],
            grata_employees_estimates_range=[0],
            headquarters={
                "exclude": [
                    {
                        "city": "city",
                        "country": "country",
                        "state": "state",
                    }
                ],
                "include": [
                    {
                        "city": "city",
                        "country": "country",
                        "example": {},
                        "state": "state",
                    }
                ],
            },
            industry_classifications={
                "exclude": [0],
                "include": [0],
            },
            is_funded=True,
            lists={
                "exclude": ["string"],
                "include": ["string"],
            },
            ownership=["string"],
            page_token="page_token",
            terms_exclude=["string"],
            terms_include={
                "group_operator": "any",
                "groups": [
                    {
                        "terms": ["string"],
                        "terms_depth": "core",
                        "terms_operator": "any",
                    }
                ],
            },
            year_founded=[0],
        )
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Grata) -> None:
        response = client.similar_search.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        similar_search = response.parse()
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Grata) -> None:
        with client.similar_search.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            similar_search = response.parse()
            assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimilarSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGrata) -> None:
        similar_search = await async_client.similar_search.create()
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGrata) -> None:
        similar_search = await async_client.similar_search.create(
            business_models=["string"],
            company_uid="26AJRCR2",
            domain="slack.com",
            employees_change=[0],
            employees_change_time="month",
            employees_on_professional_networks_range=[0],
            end_customer=["string"],
            funding_size=[0],
            funding_stage=["string"],
            grata_employees_estimates_range=[0],
            headquarters={
                "exclude": [
                    {
                        "city": "city",
                        "country": "country",
                        "state": "state",
                    }
                ],
                "include": [
                    {
                        "city": "city",
                        "country": "country",
                        "example": {},
                        "state": "state",
                    }
                ],
            },
            industry_classifications={
                "exclude": [0],
                "include": [0],
            },
            is_funded=True,
            lists={
                "exclude": ["string"],
                "include": ["string"],
            },
            ownership=["string"],
            page_token="page_token",
            terms_exclude=["string"],
            terms_include={
                "group_operator": "any",
                "groups": [
                    {
                        "terms": ["string"],
                        "terms_depth": "core",
                        "terms_operator": "any",
                    }
                ],
            },
            year_founded=[0],
        )
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGrata) -> None:
        response = await async_client.similar_search.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        similar_search = await response.parse()
        assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGrata) -> None:
        async with async_client.similar_search.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            similar_search = await response.parse()
            assert_matches_type(SimilarCompanyResponse, similar_search, path=["response"])

        assert cast(Any, response.is_closed) is True
