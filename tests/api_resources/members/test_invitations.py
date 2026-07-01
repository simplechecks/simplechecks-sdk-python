# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import Invitation
from simplechecks.types.members import InvitationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: SimpleChecks) -> None:
        invitation = client.members.invitations.create(
            email="dev@stainless.com",
            role="owner",
        )
        assert_matches_type(Invitation, invitation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: SimpleChecks) -> None:
        response = client.members.invitations.with_raw_response.create(
            email="dev@stainless.com",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(Invitation, invitation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: SimpleChecks) -> None:
        with client.members.invitations.with_streaming_response.create(
            email="dev@stainless.com",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(Invitation, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: SimpleChecks) -> None:
        invitation = client.members.invitations.list()
        assert_matches_type(InvitationListResponse, invitation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.members.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationListResponse, invitation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.members.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationListResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_revoke(self, client: SimpleChecks) -> None:
        invitation = client.members.invitations.revoke(
            "id",
        )
        assert invitation is None

    @parametrize
    def test_raw_response_revoke(self, client: SimpleChecks) -> None:
        response = client.members.invitations.with_raw_response.revoke(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert invitation is None

    @parametrize
    def test_streaming_response_revoke(self, client: SimpleChecks) -> None:
        with client.members.invitations.with_streaming_response.revoke(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert invitation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revoke(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.members.invitations.with_raw_response.revoke(
                "",
            )


class TestAsyncInvitations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSimpleChecks) -> None:
        invitation = await async_client.members.invitations.create(
            email="dev@stainless.com",
            role="owner",
        )
        assert_matches_type(Invitation, invitation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.invitations.with_raw_response.create(
            email="dev@stainless.com",
            role="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(Invitation, invitation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.invitations.with_streaming_response.create(
            email="dev@stainless.com",
            role="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(Invitation, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSimpleChecks) -> None:
        invitation = await async_client.members.invitations.list()
        assert_matches_type(InvitationListResponse, invitation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationListResponse, invitation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationListResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_revoke(self, async_client: AsyncSimpleChecks) -> None:
        invitation = await async_client.members.invitations.revoke(
            "id",
        )
        assert invitation is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.members.invitations.with_raw_response.revoke(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert invitation is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.members.invitations.with_streaming_response.revoke(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert invitation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.members.invitations.with_raw_response.revoke(
                "",
            )
