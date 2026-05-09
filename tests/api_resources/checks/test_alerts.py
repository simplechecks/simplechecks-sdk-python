# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from simplechecks import SimpleChecks, AsyncSimpleChecks

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: SimpleChecks) -> None:
        alert = client.checks.alerts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert alert is None

    @parametrize
    def test_raw_response_delete(self, client: SimpleChecks) -> None:
        response = client.checks.alerts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = response.parse()
        assert alert is None

    @parametrize
    def test_streaming_response_delete(self, client: SimpleChecks) -> None:
        with client.checks.alerts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: SimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checks.alerts.with_raw_response.delete(
                "",
            )


class TestAsyncAlerts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSimpleChecks) -> None:
        alert = await async_client.checks.alerts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert alert is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSimpleChecks) -> None:
        response = await async_client.checks.alerts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alert = await response.parse()
        assert alert is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSimpleChecks) -> None:
        async with async_client.checks.alerts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alert = await response.parse()
            assert alert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSimpleChecks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checks.alerts.with_raw_response.delete(
                "",
            )
