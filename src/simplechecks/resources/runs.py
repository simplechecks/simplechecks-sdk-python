# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import run_list_params, run_aggregates_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncRunsCursor, AsyncRunsCursor
from .._base_client import AsyncPaginator, make_request_options
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.run_detail import RunDetail
from ..types.run_list_item import RunListItem
from ..types.run_logs_response import RunLogsResponse
from ..types.run_aggregates_response import RunAggregatesResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """Read-only access to past check executions."""

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunDetail:
        """
        Returns the full record for the run matching `id` — the slim list fields plus
        the run's `metadata` (a JSON object) and a list of downloadable `artifacts`
        (each an opaque URL). Runs are retained for 30 days; an aged-out or unknown id
        returns 404. Requires the `runs:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/runs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunDetail,
        )

    def list(
        self,
        *,
        check_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        since: int | Omit = omit,
        status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"] | Omit = omit,
        until: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRunsCursor[RunListItem]:
        """Returns runs ordered by start time descending.

        Filter with `check_id`, `status`,
        `location`, and a `since`/`until` unix-millis window. `limit` defaults to 50
        (max 200). Pages are cursor-based: when more rows remain, the response carries a
        `next_cursor` — pass it back as `cursor` to fetch the next page. Requires the
        `runs:read` scope.

        Run records are served from the central runs table; runs are retained for 30
        days. Each record carries structured `provider`/`region`/`location` fields and a
        short `error_summary` rather than infrastructure internals.

        Args:
          check_id: Filter to a single check (UUID; matches `Check.id`).

          cursor: Opaque pagination token from the previous page's `next_cursor`.

          limit: Page size; defaults to 50, max 200.

          location: Filter to a single provider-native region id (e.g. `fsn1`).

          since: Lower bound on `started_at_unix_ms` (inclusive).

          status: Filter to a single execution status.

          until: Upper bound on `started_at_unix_ms` (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/runs",
            page=SyncRunsCursor[RunListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "check_id": check_id,
                        "cursor": cursor,
                        "limit": limit,
                        "location": location,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListItem,
        )

    def aggregates(
        self,
        *,
        bucket: Literal["minute"] | Omit = omit,
        check_id: str | Omit = omit,
        from_: int | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunAggregatesResponse:
        """
        Returns per-(check, location, minute-bucket) aggregate rows for the calling
        account, optionally filtered by check_id, location, and time range. Powers the
        customer dashboard ("uptime %", "pass rate", "average latency over period") and
        the public status page; you wouldn't typically render per-run rows from this
        endpoint at typical zoom levels.

        **Resolution.** Buckets are minute-aligned to UTC; the only accepted `bucket`
        value at MVP is `minute`. The param exists so future per-15s or per-hour rollups
        can slot in additively.

        **Eventual-consistency contract.** A bucket may continue to receive
        contributions after `now()` crosses its end boundary — late-arriving Garrison
        batches (network blip, scaling) feed the bucket they truncate to, which can be
        in the past. Treat any returned counts as a lower bound; dashboards refreshing
        the same window may see counts increase. The push cadence (15s) bounds how stale
        the aggregate is in steady state.

        **Latency stats.** `duration_avg_ms` is computed server-side from the underlying
        sum/count. `duration_min_ms` and `duration_max_ms` reflect the extremes seen in
        the bucket. Percentiles (p50/p95/p99) require online-mergeable sketches and are
        deferred to a follow-up.

        Requires the `runs:read` scope.

        Args:
          bucket: Bucket size. Only `minute` accepted today.

          check_id: Filter to one check.

          from_: Inclusive lower bound, unix-millis. Defaults to `now() - 1h`.

          limit: Maximum number of rows. Default 1000; hard cap 5000.

          location: Filter to one location (e.g. `hetzner`, `ovh`).

          to: Exclusive upper bound, unix-millis. Defaults to `now() + 1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/runs/aggregates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bucket": bucket,
                        "check_id": check_id,
                        "from_": from_,
                        "limit": limit,
                        "location": location,
                        "to": to,
                    },
                    run_aggregates_params.RunAggregatesParams,
                ),
            ),
            cast_to=RunAggregatesResponse,
        )

    def logs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[RunLogsResponse]:
        """Returns the gzipped JSONL execution log for the run.

        Each line is a structured
        event (timestamp, severity, source, message, optional kv map) tagged with the
        run id; producers include the executor (`run_start`, `run_end`) and per-type
        emitters (currently `http_request`, `http_response` for HTTP checks).

        The response always carries `Content-Encoding: gzip` and the bytes on the wire
        are the gzipped form; standards-compliant HTTP clients (browsers, curl,
        Go/Python/JS SDKs) decompress transparently. `sc logs <id>` (PR-Logs/2) consumes
        this endpoint.

        Tenancy is enforced before any byte fetch — a run id that doesn't belong to the
        calling account returns 404, not 403, so callers can't probe for the existence
        of other tenants' runs. Requires the `runs:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return self._get(
            path_template("/v1/runs/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[RunLogsResponse],
            stream=True,
        )


class AsyncRunsResource(AsyncAPIResource):
    """Read-only access to past check executions."""

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunDetail:
        """
        Returns the full record for the run matching `id` — the slim list fields plus
        the run's `metadata` (a JSON object) and a list of downloadable `artifacts`
        (each an opaque URL). Runs are retained for 30 days; an aged-out or unknown id
        returns 404. Requires the `runs:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/runs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunDetail,
        )

    def list(
        self,
        *,
        check_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        since: int | Omit = omit,
        status: Literal["PASS", "FAIL", "ERROR", "TIMEOUT"] | Omit = omit,
        until: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RunListItem, AsyncRunsCursor[RunListItem]]:
        """Returns runs ordered by start time descending.

        Filter with `check_id`, `status`,
        `location`, and a `since`/`until` unix-millis window. `limit` defaults to 50
        (max 200). Pages are cursor-based: when more rows remain, the response carries a
        `next_cursor` — pass it back as `cursor` to fetch the next page. Requires the
        `runs:read` scope.

        Run records are served from the central runs table; runs are retained for 30
        days. Each record carries structured `provider`/`region`/`location` fields and a
        short `error_summary` rather than infrastructure internals.

        Args:
          check_id: Filter to a single check (UUID; matches `Check.id`).

          cursor: Opaque pagination token from the previous page's `next_cursor`.

          limit: Page size; defaults to 50, max 200.

          location: Filter to a single provider-native region id (e.g. `fsn1`).

          since: Lower bound on `started_at_unix_ms` (inclusive).

          status: Filter to a single execution status.

          until: Upper bound on `started_at_unix_ms` (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/runs",
            page=AsyncRunsCursor[RunListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "check_id": check_id,
                        "cursor": cursor,
                        "limit": limit,
                        "location": location,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListItem,
        )

    async def aggregates(
        self,
        *,
        bucket: Literal["minute"] | Omit = omit,
        check_id: str | Omit = omit,
        from_: int | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        to: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunAggregatesResponse:
        """
        Returns per-(check, location, minute-bucket) aggregate rows for the calling
        account, optionally filtered by check_id, location, and time range. Powers the
        customer dashboard ("uptime %", "pass rate", "average latency over period") and
        the public status page; you wouldn't typically render per-run rows from this
        endpoint at typical zoom levels.

        **Resolution.** Buckets are minute-aligned to UTC; the only accepted `bucket`
        value at MVP is `minute`. The param exists so future per-15s or per-hour rollups
        can slot in additively.

        **Eventual-consistency contract.** A bucket may continue to receive
        contributions after `now()` crosses its end boundary — late-arriving Garrison
        batches (network blip, scaling) feed the bucket they truncate to, which can be
        in the past. Treat any returned counts as a lower bound; dashboards refreshing
        the same window may see counts increase. The push cadence (15s) bounds how stale
        the aggregate is in steady state.

        **Latency stats.** `duration_avg_ms` is computed server-side from the underlying
        sum/count. `duration_min_ms` and `duration_max_ms` reflect the extremes seen in
        the bucket. Percentiles (p50/p95/p99) require online-mergeable sketches and are
        deferred to a follow-up.

        Requires the `runs:read` scope.

        Args:
          bucket: Bucket size. Only `minute` accepted today.

          check_id: Filter to one check.

          from_: Inclusive lower bound, unix-millis. Defaults to `now() - 1h`.

          limit: Maximum number of rows. Default 1000; hard cap 5000.

          location: Filter to one location (e.g. `hetzner`, `ovh`).

          to: Exclusive upper bound, unix-millis. Defaults to `now() + 1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/runs/aggregates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bucket": bucket,
                        "check_id": check_id,
                        "from_": from_,
                        "limit": limit,
                        "location": location,
                        "to": to,
                    },
                    run_aggregates_params.RunAggregatesParams,
                ),
            ),
            cast_to=RunAggregatesResponse,
        )

    async def logs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[RunLogsResponse]:
        """Returns the gzipped JSONL execution log for the run.

        Each line is a structured
        event (timestamp, severity, source, message, optional kv map) tagged with the
        run id; producers include the executor (`run_start`, `run_end`) and per-type
        emitters (currently `http_request`, `http_response` for HTTP checks).

        The response always carries `Content-Encoding: gzip` and the bytes on the wire
        are the gzipped form; standards-compliant HTTP clients (browsers, curl,
        Go/Python/JS SDKs) decompress transparently. `sc logs <id>` (PR-Logs/2) consumes
        this endpoint.

        Tenancy is enforced before any byte fetch — a run id that doesn't belong to the
        calling account returns 404, not 403, so callers can't probe for the existence
        of other tenants' runs. Requires the `runs:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/runs/{id}/logs", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[RunLogsResponse],
            stream=True,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.aggregates = to_raw_response_wrapper(
            runs.aggregates,
        )
        self.logs = to_raw_response_wrapper(
            runs.logs,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.aggregates = async_to_raw_response_wrapper(
            runs.aggregates,
        )
        self.logs = async_to_raw_response_wrapper(
            runs.logs,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.aggregates = to_streamed_response_wrapper(
            runs.aggregates,
        )
        self.logs = to_streamed_response_wrapper(
            runs.logs,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.aggregates = async_to_streamed_response_wrapper(
            runs.aggregates,
        )
        self.logs = async_to_streamed_response_wrapper(
            runs.logs,
        )
