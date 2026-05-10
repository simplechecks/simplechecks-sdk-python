# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import CheckoutSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SimpleChecks) -> None:
        checkout_session = client.checkout_sessions.create(
            bundle_sku="starter",
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SimpleChecks) -> None:
        response = client.checkout_sessions.with_raw_response.create(
            bundle_sku="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = response.parse()
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SimpleChecks) -> None:
        with client.checkout_sessions.with_streaming_response.create(
            bundle_sku="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = response.parse()
            assert_matches_type(CheckoutSession, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckoutSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSimpleChecks) -> None:
        checkout_session = await async_client.checkout_sessions.create(
            bundle_sku="starter",
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.checkout_sessions.with_raw_response.create(
            bundle_sku="starter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = await response.parse()
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.checkout_sessions.with_streaming_response.create(
            bundle_sku="starter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = await response.parse()
            assert_matches_type(CheckoutSession, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True
