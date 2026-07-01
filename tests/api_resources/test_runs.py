# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from simplechecks import SimpleChecks, AsyncSimpleChecks
from simplechecks.types import (
    RunDetail,
    RunListItem,
    RunLogsResponse,
    RunAggregatesResponse,
)
from simplechecks.pagination import SyncRunsCursor, AsyncRunsCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: SimpleChecks) -> None:
        run = client.runs.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        assert_matches_type(RunDetail, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunDetail, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunDetail, run, path=["response"])

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
        assert_matches_type(SyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: SimpleChecks) -> None:
        run = client.runs.list(
            check_id="check_id",
            cursor="cursor",
            limit=0,
            location="location",
            since=0,
            status="PASS",
            until=0,
        )
        assert_matches_type(SyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncRunsCursor[RunListItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_aggregates(self, client: SimpleChecks) -> None:
        run = client.runs.aggregates()
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    def test_method_aggregates_with_all_params(self, client: SimpleChecks) -> None:
        run = client.runs.aggregates(
            bucket="minute",
            check_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_=0,
            limit=0,
            location="location",
            to=0,
        )
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    def test_raw_response_aggregates(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.aggregates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_aggregates(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.aggregates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunAggregatesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logs(self, client: SimpleChecks) -> None:
        run_stream = client.runs.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        for item in run_stream:
            assert_matches_type(RunLogsResponse, item, path=["response"])

    @parametrize
    def test_raw_response_logs(self, client: SimpleChecks) -> None:
        response = client.runs.with_raw_response.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        for item in stream:
            assert_matches_type(RunLogsResponse, item, path=["line"])

    @parametrize
    def test_streaming_response_logs(self, client: SimpleChecks) -> None:
        with client.runs.with_streaming_response.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            for item in stream:
                assert_matches_type(RunLogsResponse, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_logs(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.runs.with_raw_response.logs(
                "",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        assert_matches_type(RunDetail, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunDetail, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.retrieve(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunDetail, run, path=["response"])

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
        assert_matches_type(AsyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.list(
            check_id="check_id",
            cursor="cursor",
            limit=0,
            location="location",
            since=0,
            status="PASS",
            until=0,
        )
        assert_matches_type(AsyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncRunsCursor[RunListItem], run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncRunsCursor[RunListItem], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_aggregates(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.aggregates()
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    async def test_method_aggregates_with_all_params(self, async_client: AsyncSimpleChecks) -> None:
        run = await async_client.runs.aggregates(
            bucket="minute",
            check_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_=0,
            limit=0,
            location="location",
            to=0,
        )
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_aggregates(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.aggregates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunAggregatesResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_aggregates(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.aggregates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunAggregatesResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logs(self, async_client: AsyncSimpleChecks) -> None:
        run_stream = await async_client.runs.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )
        async for item in run_stream:
            assert_matches_type(RunLogsResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.runs.with_raw_response.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        async for item in stream:
            assert_matches_type(RunLogsResponse, item, path=["line"])

    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.runs.with_streaming_response.logs(
            "run_sew2vlfw09vz231q9mz9al2ecd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            async for item in stream:
                assert_matches_type(RunLogsResponse, item, path=["item"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_logs(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.runs.with_raw_response.logs(
                "",
            )
