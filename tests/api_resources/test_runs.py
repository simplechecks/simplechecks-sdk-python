# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import Run, RunListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SimpleChecks) -> None:
        run = client.runs.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.runs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: SimpleChecks) -> None:
        run = client.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SimpleChecks) -> None:
        run = client.runs.list(
            check_id="check_id",
            limit=0,
            offset=0,
            since=0,
            status="PASS",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.runs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.list()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.list(
            check_id="check_id",
            limit=0,
            offset=0,
            since=0,
            status="PASS",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True
