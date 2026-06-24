# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import maintenance_window_list_params, maintenance_window_create_params, maintenance_window_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncMaintenanceWindowsCursor, AsyncMaintenanceWindowsCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.maintenance_window import MaintenanceWindow

__all__ = ["MaintenanceWindowsResource", "AsyncMaintenanceWindowsResource"]


class MaintenanceWindowsResource(SyncAPIResource):
    """
    Account-scoped windows that pause execution of their targeted
    checks for the scheduled interval(s); paused runs are not recorded
    and never count against uptime.
    """

    @cached_property
    def with_raw_response(self) -> MaintenanceWindowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MaintenanceWindowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MaintenanceWindowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return MaintenanceWindowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        duration_ms: int,
        name: str,
        schedule_kind: Literal["one_time", "recurring"],
        start_unix_ms: int,
        check_ids: SequenceNotStr[str] | Omit = omit,
        check_tags: SequenceNotStr[str] | Omit = omit,
        repeat_ends_unix_ms: int | Omit = omit,
        repeat_interval: int | Omit = omit,
        repeat_unit: Literal["DAY", "WEEK", "MONTH"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaintenanceWindow:
        """
        Creates a maintenance window that pauses execution of its targeted checks for
        the scheduled interval(s). `schedule_kind` is `one_time` or `recurring`;
        recurrence fields (`repeat_unit`, `repeat_interval`, `repeat_ends_unix_ms`) are
        valid only for a recurring window. `timezone` is an IANA name. `check_ids` are
        raw check UUIDs and must belong to your account; a check id that doesn't
        returns 404. Requires the `alerts:write` scope (owner/admin only).

        Args:
          duration_ms: Window duration in milliseconds; must be positive.

          check_ids: Raw check UUIDs to target (must belong to your account).

          repeat_ends_unix_ms: Valid only for a recurring window.

          repeat_interval: Valid only for a recurring window; must be positive.

          repeat_unit: Valid only for a recurring window.

          timezone: IANA timezone name. Defaults to UTC when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/maintenance-windows",
            body=maybe_transform(
                {
                    "duration_ms": duration_ms,
                    "name": name,
                    "schedule_kind": schedule_kind,
                    "start_unix_ms": start_unix_ms,
                    "check_ids": check_ids,
                    "check_tags": check_tags,
                    "repeat_ends_unix_ms": repeat_ends_unix_ms,
                    "repeat_interval": repeat_interval,
                    "repeat_unit": repeat_unit,
                    "timezone": timezone,
                },
                maintenance_window_create_params.MaintenanceWindowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

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
    ) -> MaintenanceWindow:
        """Returns the window with its targeting.

        404 if no such window exists for the
        calling account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/maintenance-windows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

    def update(
        self,
        id: str,
        *,
        check_ids: SequenceNotStr[str] | Omit = omit,
        check_tags: SequenceNotStr[str] | Omit = omit,
        duration_ms: int | Omit = omit,
        name: str | Omit = omit,
        repeat_ends_unix_ms: int | Omit = omit,
        repeat_interval: int | Omit = omit,
        repeat_unit: Literal["DAY", "WEEK", "MONTH"] | Omit = omit,
        schedule_kind: Literal["one_time", "recurring"] | Omit = omit,
        start_unix_ms: int | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaintenanceWindow:
        """Updates the supplied fields.

        A non-null `check_ids` replaces the targeting set;
        a check id that isn't your account's returns 404. The effective schedule is
        re-validated. Omitted fields are unchanged. Requires the `alerts:write` scope
        (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/maintenance-windows/{id}", id=id),
            body=maybe_transform(
                {
                    "check_ids": check_ids,
                    "check_tags": check_tags,
                    "duration_ms": duration_ms,
                    "name": name,
                    "repeat_ends_unix_ms": repeat_ends_unix_ms,
                    "repeat_interval": repeat_interval,
                    "repeat_unit": repeat_unit,
                    "schedule_kind": schedule_kind,
                    "start_unix_ms": start_unix_ms,
                    "timezone": timezone,
                },
                maintenance_window_update_params.MaintenanceWindowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMaintenanceWindowsCursor[MaintenanceWindow]:
        """Returns the caller's maintenance windows with cursor pagination.

        Each window
        carries its explicit check targeting (`check_ids`). `next_cursor` is set when a
        full page was returned and null on the final page. Requires the `alerts:read`
        scope.

        Args:
          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/maintenance-windows",
            page=SyncMaintenanceWindowsCursor[MaintenanceWindow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    maintenance_window_list_params.MaintenanceWindowListParams,
                ),
            ),
            model=MaintenanceWindow,
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
        """
        Removes the window and its targeting; affected checks resume normal execution.
        Requires the `alerts:write` scope (owner/admin only).

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
            path_template("/v1/maintenance-windows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMaintenanceWindowsResource(AsyncAPIResource):
    """
    Account-scoped windows that pause execution of their targeted
    checks for the scheduled interval(s); paused runs are not recorded
    and never count against uptime.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMaintenanceWindowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMaintenanceWindowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMaintenanceWindowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncMaintenanceWindowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        duration_ms: int,
        name: str,
        schedule_kind: Literal["one_time", "recurring"],
        start_unix_ms: int,
        check_ids: SequenceNotStr[str] | Omit = omit,
        check_tags: SequenceNotStr[str] | Omit = omit,
        repeat_ends_unix_ms: int | Omit = omit,
        repeat_interval: int | Omit = omit,
        repeat_unit: Literal["DAY", "WEEK", "MONTH"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaintenanceWindow:
        """
        Creates a maintenance window that pauses execution of its targeted checks for
        the scheduled interval(s). `schedule_kind` is `one_time` or `recurring`;
        recurrence fields (`repeat_unit`, `repeat_interval`, `repeat_ends_unix_ms`) are
        valid only for a recurring window. `timezone` is an IANA name. `check_ids` are
        raw check UUIDs and must belong to your account; a check id that doesn't
        returns 404. Requires the `alerts:write` scope (owner/admin only).

        Args:
          duration_ms: Window duration in milliseconds; must be positive.

          check_ids: Raw check UUIDs to target (must belong to your account).

          repeat_ends_unix_ms: Valid only for a recurring window.

          repeat_interval: Valid only for a recurring window; must be positive.

          repeat_unit: Valid only for a recurring window.

          timezone: IANA timezone name. Defaults to UTC when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/maintenance-windows",
            body=await async_maybe_transform(
                {
                    "duration_ms": duration_ms,
                    "name": name,
                    "schedule_kind": schedule_kind,
                    "start_unix_ms": start_unix_ms,
                    "check_ids": check_ids,
                    "check_tags": check_tags,
                    "repeat_ends_unix_ms": repeat_ends_unix_ms,
                    "repeat_interval": repeat_interval,
                    "repeat_unit": repeat_unit,
                    "timezone": timezone,
                },
                maintenance_window_create_params.MaintenanceWindowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

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
    ) -> MaintenanceWindow:
        """Returns the window with its targeting.

        404 if no such window exists for the
        calling account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/maintenance-windows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

    async def update(
        self,
        id: str,
        *,
        check_ids: SequenceNotStr[str] | Omit = omit,
        check_tags: SequenceNotStr[str] | Omit = omit,
        duration_ms: int | Omit = omit,
        name: str | Omit = omit,
        repeat_ends_unix_ms: int | Omit = omit,
        repeat_interval: int | Omit = omit,
        repeat_unit: Literal["DAY", "WEEK", "MONTH"] | Omit = omit,
        schedule_kind: Literal["one_time", "recurring"] | Omit = omit,
        start_unix_ms: int | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MaintenanceWindow:
        """Updates the supplied fields.

        A non-null `check_ids` replaces the targeting set;
        a check id that isn't your account's returns 404. The effective schedule is
        re-validated. Omitted fields are unchanged. Requires the `alerts:write` scope
        (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/maintenance-windows/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "check_ids": check_ids,
                    "check_tags": check_tags,
                    "duration_ms": duration_ms,
                    "name": name,
                    "repeat_ends_unix_ms": repeat_ends_unix_ms,
                    "repeat_interval": repeat_interval,
                    "repeat_unit": repeat_unit,
                    "schedule_kind": schedule_kind,
                    "start_unix_ms": start_unix_ms,
                    "timezone": timezone,
                },
                maintenance_window_update_params.MaintenanceWindowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MaintenanceWindow,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MaintenanceWindow, AsyncMaintenanceWindowsCursor[MaintenanceWindow]]:
        """Returns the caller's maintenance windows with cursor pagination.

        Each window
        carries its explicit check targeting (`check_ids`). `next_cursor` is set when a
        full page was returned and null on the final page. Requires the `alerts:read`
        scope.

        Args:
          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/maintenance-windows",
            page=AsyncMaintenanceWindowsCursor[MaintenanceWindow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    maintenance_window_list_params.MaintenanceWindowListParams,
                ),
            ),
            model=MaintenanceWindow,
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
        """
        Removes the window and its targeting; affected checks resume normal execution.
        Requires the `alerts:write` scope (owner/admin only).

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
            path_template("/v1/maintenance-windows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MaintenanceWindowsResourceWithRawResponse:
    def __init__(self, maintenance_windows: MaintenanceWindowsResource) -> None:
        self._maintenance_windows = maintenance_windows

        self.create = to_raw_response_wrapper(
            maintenance_windows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            maintenance_windows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            maintenance_windows.update,
        )
        self.list = to_raw_response_wrapper(
            maintenance_windows.list,
        )
        self.delete = to_raw_response_wrapper(
            maintenance_windows.delete,
        )


class AsyncMaintenanceWindowsResourceWithRawResponse:
    def __init__(self, maintenance_windows: AsyncMaintenanceWindowsResource) -> None:
        self._maintenance_windows = maintenance_windows

        self.create = async_to_raw_response_wrapper(
            maintenance_windows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            maintenance_windows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            maintenance_windows.update,
        )
        self.list = async_to_raw_response_wrapper(
            maintenance_windows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            maintenance_windows.delete,
        )


class MaintenanceWindowsResourceWithStreamingResponse:
    def __init__(self, maintenance_windows: MaintenanceWindowsResource) -> None:
        self._maintenance_windows = maintenance_windows

        self.create = to_streamed_response_wrapper(
            maintenance_windows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            maintenance_windows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            maintenance_windows.update,
        )
        self.list = to_streamed_response_wrapper(
            maintenance_windows.list,
        )
        self.delete = to_streamed_response_wrapper(
            maintenance_windows.delete,
        )


class AsyncMaintenanceWindowsResourceWithStreamingResponse:
    def __init__(self, maintenance_windows: AsyncMaintenanceWindowsResource) -> None:
        self._maintenance_windows = maintenance_windows

        self.create = async_to_streamed_response_wrapper(
            maintenance_windows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            maintenance_windows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            maintenance_windows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            maintenance_windows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            maintenance_windows.delete,
        )
