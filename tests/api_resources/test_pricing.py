# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import Pricing

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPricing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SimpleChecks) -> None:
        pricing = client.pricing.retrieve()
        assert_matches_type(Pricing, pricing, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SimpleChecks) -> None:
        response = client.pricing.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing = response.parse()
        assert_matches_type(Pricing, pricing, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SimpleChecks) -> None:
        with client.pricing.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing = response.parse()
            assert_matches_type(Pricing, pricing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPricing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        pricing = await async_client.pricing.retrieve()
        assert_matches_type(Pricing, pricing, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.pricing.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pricing = await response.parse()
        assert_matches_type(Pricing, pricing, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.pricing.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pricing = await response.parse()
            assert_matches_type(Pricing, pricing, path=["response"])

        assert cast(Any, response.is_closed) is True
