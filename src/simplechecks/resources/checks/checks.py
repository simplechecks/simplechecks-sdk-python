# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .alerts import (
    AlertsResource,
    AsyncAlertsResource,
    AlertsResourceWithRawResponse,
    AsyncAlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ChecksResource", "AsyncChecksResource"]


class ChecksResource(SyncAPIResource):
    """CRUD for synthetic-monitoring checks."""

    @cached_property
    def alerts(self) -> AlertsResource:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return ChecksResourceWithStreamingResponse(self)

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
        """Disables the check.

        Requires the `checks:write` scope.

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
            path_template("/v1/checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChecksResource(AsyncAPIResource):
    """CRUD for synthetic-monitoring checks."""

    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AsyncAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncChecksResourceWithStreamingResponse(self)

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
        """Disables the check.

        Requires the `checks:write` scope.

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
            path_template("/v1/checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChecksResourceWithRawResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.delete = to_raw_response_wrapper(
            checks.delete,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AlertsResourceWithRawResponse(self._checks.alerts)


class AsyncChecksResourceWithRawResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.delete = async_to_raw_response_wrapper(
            checks.delete,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AsyncAlertsResourceWithRawResponse(self._checks.alerts)


class ChecksResourceWithStreamingResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.delete = to_streamed_response_wrapper(
            checks.delete,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AlertsResourceWithStreamingResponse(self._checks.alerts)


class AsyncChecksResourceWithStreamingResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.delete = async_to_streamed_response_wrapper(
            checks.delete,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        """Per-check alert configuration + test-fire endpoint (PR-Alerts/1)."""
        return AsyncAlertsResourceWithStreamingResponse(self._checks.alerts)
