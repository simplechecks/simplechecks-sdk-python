# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import KeyListResponse, KeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SimpleChecks) -> None:
        key = client.keys.create(
            name="name",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: SimpleChecks) -> None:
        key = client.keys.create(
            name="name",
            scopes=["string"],
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SimpleChecks) -> None:
        response = client.keys.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SimpleChecks) -> None:
        with client.keys.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SimpleChecks) -> None:
        key = client.keys.list()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_revoke(self, client: SimpleChecks) -> None:
        key = client.keys.revoke(
            "id",
        )
        assert key is None

    @parametrize
    def test_raw_response_revoke(self, client: SimpleChecks) -> None:
        response = client.keys.with_raw_response.revoke(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert key is None

    @parametrize
    def test_streaming_response_revoke(self, client: SimpleChecks) -> None:
        with client.keys.with_streaming_response.revoke(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.keys.with_raw_response.revoke(
                "",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSimpleChecks) -> None:
        key = await async_client.keys.create(
            name="name",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSimpleChecks) -> None:
        key = await async_client.keys.create(
            name="name",
            scopes=["string"],
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.keys.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.keys.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSimpleChecks) -> None:
        key = await async_client.keys.list()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_revoke(self, async_client: AsyncSimpleChecks) -> None:
        key = await async_client.keys.revoke(
            "id",
        )
        assert key is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.keys.with_raw_response.revoke(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert key is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.keys.with_streaming_response.revoke(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert key is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.keys.with_raw_response.revoke(
                "",
            )
