# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import Simplechecks, AsyncSimplechecks
from simplechecks.types import Check, CheckListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Simplechecks) -> None:
        check = client.checks.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Simplechecks) -> None:
        check = client.checks.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
            artifact_url="artifact_url",
            config={"foo": "bar"},
            timeout_ms=0,
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Simplechecks) -> None:
        response = client.checks.with_raw_response.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Simplechecks) -> None:
        with client.checks.with_streaming_response.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Simplechecks) -> None:
        check = client.checks.retrieve(
            "id",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Simplechecks) -> None:
        response = client.checks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Simplechecks) -> None:
        with client.checks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Simplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Simplechecks) -> None:
        check = client.checks.update(
            id="id",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Simplechecks) -> None:
        check = client.checks.update(
            id="id",
            artifact_url="artifact_url",
            config={"foo": "bar"},
            enabled=True,
            name="name",
            schedule="schedule",
            target_url="https://example.com",
            timeout_ms=0,
            type="type",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Simplechecks) -> None:
        response = client.checks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Simplechecks) -> None:
        with client.checks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Simplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Simplechecks) -> None:
        check = client.checks.list()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Simplechecks) -> None:
        check = client.checks.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Simplechecks) -> None:
        response = client.checks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Simplechecks) -> None:
        with client.checks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(CheckListResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Simplechecks) -> None:
        check = client.checks.delete(
            "id",
        )
        assert check is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Simplechecks) -> None:
        response = client.checks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert check is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Simplechecks) -> None:
        with client.checks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Simplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checks.with_raw_response.delete(
                "",
            )


class TestAsyncChecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
            artifact_url="artifact_url",
            config={"foo": "bar"},
            timeout_ms=0,
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSimplechecks) -> None:
        response = await async_client.checks.with_raw_response.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSimplechecks) -> None:
        async with async_client.checks.with_streaming_response.create(
            enabled=True,
            location="location",
            name="name",
            provider="provider",
            schedule="*/5 * * * *",
            target_url="https://example.com",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.retrieve(
            "id",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSimplechecks) -> None:
        response = await async_client.checks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSimplechecks) -> None:
        async with async_client.checks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSimplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.update(
            id="id",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.update(
            id="id",
            artifact_url="artifact_url",
            config={"foo": "bar"},
            enabled=True,
            name="name",
            schedule="schedule",
            target_url="https://example.com",
            timeout_ms=0,
            type="type",
        )
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSimplechecks) -> None:
        response = await async_client.checks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(Check, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSimplechecks) -> None:
        async with async_client.checks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(Check, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSimplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.list()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimplechecks) -> None:
        response = await async_client.checks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimplechecks) -> None:
        async with async_client.checks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(CheckListResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSimplechecks) -> None:
        check = await async_client.checks.delete(
            "id",
        )
        assert check is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSimplechecks) -> None:
        response = await async_client.checks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert check is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSimplechecks) -> None:
        async with async_client.checks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSimplechecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checks.with_raw_response.delete(
                "",
            )
