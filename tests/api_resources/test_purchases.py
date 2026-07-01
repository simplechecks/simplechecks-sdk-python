# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import PurchaseListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: SimpleChecks) -> None:
        purchase = client.purchases.list()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SimpleChecks) -> None:
        purchase = client.purchases.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.purchases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.purchases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseListResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPurchases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncSimpleChecks) -> None:
        purchase = await async_client.purchases.list()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSimpleChecks) -> None:
        purchase = await async_client.purchases.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.purchases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseListResponse, purchase, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.purchases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseListResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True
