# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import Member, MemberListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: SimpleChecks) -> None:
        member = client.members.update(
            user_id="user_id",
            role="owner",
        )
        assert_matches_type(Member, member, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: SimpleChecks) -> None:
        response = client.members.with_raw_response.update(
            user_id="user_id",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Member, member, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: SimpleChecks) -> None:
        with client.members.with_streaming_response.update(
            user_id="user_id",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Member, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.members.with_raw_response.update(
                user_id="",
                role="owner",
            )

    @parametrize
    def test_method_list(self, client: SimpleChecks) -> None:
        member = client.members.list()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MemberListResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: SimpleChecks) -> None:
        member = client.members.remove(
            "user_id",
        )
        assert member is None

    @parametrize
    def test_raw_response_remove(self, client: SimpleChecks) -> None:
        response = client.members.with_raw_response.remove(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @parametrize
    def test_streaming_response_remove(self, client: SimpleChecks) -> None:
        with client.members.with_streaming_response.remove(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.members.with_raw_response.remove(
                "",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncSimpleChecks) -> None:
        member = await async_client.members.update(
            user_id="user_id",
            role="owner",
        )
        assert_matches_type(Member, member, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.with_raw_response.update(
            user_id="user_id",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Member, member, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.with_streaming_response.update(
            user_id="user_id",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Member, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.members.with_raw_response.update(
                user_id="",
                role="owner",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSimpleChecks) -> None:
        member = await async_client.members.list()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MemberListResponse, member, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MemberListResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncSimpleChecks) -> None:
        member = await async_client.members.remove(
            "user_id",
        )
        assert member is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.with_raw_response.remove(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.with_streaming_response.remove(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.members.with_raw_response.remove(
                "",
            )
