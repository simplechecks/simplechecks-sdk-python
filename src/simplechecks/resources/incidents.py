# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import incident_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.incident_list_response import IncidentListResponse

__all__ = ["IncidentsResource", "AsyncIncidentsResource"]


class IncidentsResource(SyncAPIResource):
    """Read-only incident timeline derived from alert state."""

    @cached_property
    def with_raw_response(self) -> IncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return IncidentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IncidentListResponse:
        """
        Returns incidents derived on read from `alert_state` (ongoing) and
        `alert_dispatches` (resolved). Ordered ongoing-first, then most-recent-resolved
        first. Pagination is offset-based; pass `next_offset` back to continue.

        Status semantics:

        - `ongoing` — `alert_state.current_incident_id` is set; `resolved_at_unix_ms` is
          omitted.
        - `resolved` — a recovery dispatch has been enqueued; both timestamps are
          populated.

        Incidents that fired entirely inside a maintenance window won't appear here —
        the dispatcher doesn't ledger suppressed dispatches. That matches the customer
        expectation that maintenance windows mean "don't notify, don't surface as
        urgent."

        Requires the `checks:read` scope (incidents are per-check; we reuse the existing
        scope rather than minting a new one).

        Args:
          limit: Max number of incidents to return. Defaults to 50; server caps at 500.

          offset: Number of incidents to skip. Pass the `next_offset` from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/incidents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    incident_list_params.IncidentListParams,
                ),
            ),
            cast_to=IncidentListResponse,
        )


class AsyncIncidentsResource(AsyncAPIResource):
    """Read-only incident timeline derived from alert state."""

    @cached_property
    def with_raw_response(self) -> AsyncIncidentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncidentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncidentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncIncidentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IncidentListResponse:
        """
        Returns incidents derived on read from `alert_state` (ongoing) and
        `alert_dispatches` (resolved). Ordered ongoing-first, then most-recent-resolved
        first. Pagination is offset-based; pass `next_offset` back to continue.

        Status semantics:

        - `ongoing` — `alert_state.current_incident_id` is set; `resolved_at_unix_ms` is
          omitted.
        - `resolved` — a recovery dispatch has been enqueued; both timestamps are
          populated.

        Incidents that fired entirely inside a maintenance window won't appear here —
        the dispatcher doesn't ledger suppressed dispatches. That matches the customer
        expectation that maintenance windows mean "don't notify, don't surface as
        urgent."

        Requires the `checks:read` scope (incidents are per-check; we reuse the existing
        scope rather than minting a new one).

        Args:
          limit: Max number of incidents to return. Defaults to 50; server caps at 500.

          offset: Number of incidents to skip. Pass the `next_offset` from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/incidents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    incident_list_params.IncidentListParams,
                ),
            ),
            cast_to=IncidentListResponse,
        )


class IncidentsResourceWithRawResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.list = to_raw_response_wrapper(
            incidents.list,
        )


class AsyncIncidentsResourceWithRawResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.list = async_to_raw_response_wrapper(
            incidents.list,
        )


class IncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: IncidentsResource) -> None:
        self._incidents = incidents

        self.list = to_streamed_response_wrapper(
            incidents.list,
        )


class AsyncIncidentsResourceWithStreamingResponse:
    def __init__(self, incidents: AsyncIncidentsResource) -> None:
        self._incidents = incidents

        self.list = async_to_streamed_response_wrapper(
            incidents.list,
        )
