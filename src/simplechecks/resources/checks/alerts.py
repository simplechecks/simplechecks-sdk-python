# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.checks import alert_replace_params
from ...types.alert_config import AlertConfig

__all__ = ["AlertsResource", "AsyncAlertsResource"]


class AlertsResource(SyncAPIResource):
    """
    Per-check alert settings: consecutive-failure threshold and the
    M-of-N consensus parameters. Notification destinations are
    reusable account-scoped resources under `alert-channels`, bound to
    checks via `alert-subscriptions`.
    """

    @cached_property
    def with_raw_response(self) -> AlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AlertsResourceWithStreamingResponse(self)

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
    ) -> AlertConfig:
        """
        Returns the per-check alert configuration: enabled flag, thresholds, M-of-N
        consensus, maintenance windows, channels. Requires the `checks:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/checks/{id}/alerts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertConfig,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Subsequent runs will not be evaluated for alerts.

        State rows in `alert_state`
        and `alert_location_state` cascade with the underlying check; deleting just the
        config leaves them behind harmlessly. Requires the `checks:write` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/checks/{id}/alerts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        id: str,
        *,
        consecutive_failures_threshold: int,
        consensus_m: int,
        consensus_n: int,
        enabled: bool,
        account_id: str | Omit = omit,
        check_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertConfig:
        """Idempotent upsert.

        The same body shape is returned by GET. This configures alert
        _settings_ only (failure threshold + consensus); notification destinations live
        in `alert-channels`, bound via `alert-subscriptions`. The evaluator runs M-of-N
        consensus before incident-firing; if fewer than `consensus_m` locations have
        observations, the rule falls back to "any failing = failing" so brand-new checks
        don't miss outages.

        Eventual-consistency contract: after a config write, the evaluator picks up the
        new thresholds on the next ingest cycle (15s push cadence).

        Requires the `checks:write` scope.

        Args:
          consecutive_failures_threshold: Number of consecutive globally-failing observations (after M-of-N consensus
              collapses per-location status) required before an incident fires. Default = 1 =
              "alert on first globally-failing observation."

          consensus_m: M-of-N consensus rule denominator (expected total location count). When fewer
              than `consensus_m` locations have observations, the evaluator falls back to "any
              failing = failing" so brand-new checks don't miss outages.

          consensus_n: M-of-N consensus rule numerator. The evaluator considers the check
              globally-failing only when at least this many locations are reporting fail
              concurrently.

          enabled: When false, the evaluator skips this check entirely.

          account_id: Server-set; ignored on write.

          check_id: Server-set; ignored on write.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v1/checks/{id}/alerts", id=id),
            body=maybe_transform(
                {
                    "consecutive_failures_threshold": consecutive_failures_threshold,
                    "consensus_m": consensus_m,
                    "consensus_n": consensus_n,
                    "enabled": enabled,
                    "account_id": account_id,
                    "check_id": check_id,
                },
                alert_replace_params.AlertReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertConfig,
        )


class AsyncAlertsResource(AsyncAPIResource):
    """
    Per-check alert settings: consecutive-failure threshold and the
    M-of-N consensus parameters. Notification destinations are
    reusable account-scoped resources under `alert-channels`, bound to
    checks via `alert-subscriptions`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncAlertsResourceWithStreamingResponse(self)

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
    ) -> AlertConfig:
        """
        Returns the per-check alert configuration: enabled flag, thresholds, M-of-N
        consensus, maintenance windows, channels. Requires the `checks:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/checks/{id}/alerts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertConfig,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Subsequent runs will not be evaluated for alerts.

        State rows in `alert_state`
        and `alert_location_state` cascade with the underlying check; deleting just the
        config leaves them behind harmlessly. Requires the `checks:write` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/checks/{id}/alerts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        id: str,
        *,
        consecutive_failures_threshold: int,
        consensus_m: int,
        consensus_n: int,
        enabled: bool,
        account_id: str | Omit = omit,
        check_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertConfig:
        """Idempotent upsert.

        The same body shape is returned by GET. This configures alert
        _settings_ only (failure threshold + consensus); notification destinations live
        in `alert-channels`, bound via `alert-subscriptions`. The evaluator runs M-of-N
        consensus before incident-firing; if fewer than `consensus_m` locations have
        observations, the rule falls back to "any failing = failing" so brand-new checks
        don't miss outages.

        Eventual-consistency contract: after a config write, the evaluator picks up the
        new thresholds on the next ingest cycle (15s push cadence).

        Requires the `checks:write` scope.

        Args:
          consecutive_failures_threshold: Number of consecutive globally-failing observations (after M-of-N consensus
              collapses per-location status) required before an incident fires. Default = 1 =
              "alert on first globally-failing observation."

          consensus_m: M-of-N consensus rule denominator (expected total location count). When fewer
              than `consensus_m` locations have observations, the evaluator falls back to "any
              failing = failing" so brand-new checks don't miss outages.

          consensus_n: M-of-N consensus rule numerator. The evaluator considers the check
              globally-failing only when at least this many locations are reporting fail
              concurrently.

          enabled: When false, the evaluator skips this check entirely.

          account_id: Server-set; ignored on write.

          check_id: Server-set; ignored on write.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v1/checks/{id}/alerts", id=id),
            body=await async_maybe_transform(
                {
                    "consecutive_failures_threshold": consecutive_failures_threshold,
                    "consensus_m": consensus_m,
                    "consensus_n": consensus_n,
                    "enabled": enabled,
                    "account_id": account_id,
                    "check_id": check_id,
                },
                alert_replace_params.AlertReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertConfig,
        )


class AlertsResourceWithRawResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            alerts.delete,
        )
        self.replace = to_raw_response_wrapper(
            alerts.replace,
        )


class AsyncAlertsResourceWithRawResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            alerts.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            alerts.replace,
        )


class AlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            alerts.delete,
        )
        self.replace = to_streamed_response_wrapper(
            alerts.replace,
        )


class AsyncAlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            alerts.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            alerts.replace,
        )
