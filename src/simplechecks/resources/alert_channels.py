# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import alert_channel_list_params, alert_channel_create_params, alert_channel_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncAlertChannelsCursor, AsyncAlertChannelsCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.alert_channel import AlertChannel
from ..types.alert_channel_test_fire_response import AlertChannelTestFireResponse

__all__ = ["AlertChannelsResource", "AsyncAlertChannelsResource"]


class AlertChannelsResource(SyncAPIResource):
    """
    Reusable, account-scoped notification destinations (webhook,
    Slack, Discord, Teams, PagerDuty, Opsgenie, email). One channel
    can serve many checks. Includes a test-fire endpoint.
    """

    @cached_property
    def with_raw_response(self) -> AlertChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlertChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AlertChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        target: str,
        type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"],
        config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannel:
        """Creates a reusable notification destination.

        URL-bearing types (`webhook`,
        `slack`, `discord`, `teams`) are SSRF-filtered: targets resolving to private,
        loopback, or link-local addresses are rejected. The `target` is write-only —
        it's masked on every read. Requires the `alerts:write` scope (owner/admin only).

        Args:
          target: Destination secret. URL for the webhook flavors (slack/discord/teams/webhook),
              email address for `email`, integration key for `pagerduty`, API key for
              `opsgenie`. URL-bearing types are SSRF-filtered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alert-channels",
            body=maybe_transform(
                {
                    "name": name,
                    "target": target,
                    "type": type,
                    "config": config,
                },
                alert_channel_create_params.AlertChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
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
    ) -> AlertChannel:
        """Returns the alert channel.

        The `target` secret is masked. 404 if no such channel
        exists for the calling account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/alert-channels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
        )

    def update(
        self,
        id: str,
        *,
        config: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        target: str | Omit = omit,
        type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannel:
        """All fields are optional; omitted fields are unchanged.

        A `target` equal to the
        masked value (`***<last4>`) is a no-op — only a fresh, non-masked secret updates
        the stored target. Requires the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/alert-channels/{id}", id=id),
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "target": target,
                    "type": type,
                },
                alert_channel_update_params.AlertChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
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
    ) -> SyncAlertChannelsCursor[AlertChannel]:
        """
        Returns the caller's reusable alert channels with cursor pagination.
        `next_cursor` is set when a full page was returned and null on the final page.
        The `target` secret is always masked (`***<last4>`); the raw value is never
        returned. Requires the `alerts:read` scope.

        Args:
          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/alert-channels",
            page=SyncAlertChannelsCursor[AlertChannel],
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
                    alert_channel_list_params.AlertChannelListParams,
                ),
            ),
            model=AlertChannel,
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
        Deletes the channel and cascades its subscriptions (the bound checks simply stop
        notifying it). Requires the `alerts:write` scope (owner/admin only).

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
            path_template("/v1/alert-channels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test_fire(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannelTestFireResponse:
        """
        Enqueues a single `test_fire` dispatch through the channel so a customer can
        verify the destination works. Idempotent on the channel id (repeated clicks
        dedup). Requires the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/alert-channels/{id}:test", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannelTestFireResponse,
        )


class AsyncAlertChannelsResource(AsyncAPIResource):
    """
    Reusable, account-scoped notification destinations (webhook,
    Slack, Discord, Teams, PagerDuty, Opsgenie, email). One channel
    can serve many checks. Includes a test-fire endpoint.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAlertChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncAlertChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        target: str,
        type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"],
        config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannel:
        """Creates a reusable notification destination.

        URL-bearing types (`webhook`,
        `slack`, `discord`, `teams`) are SSRF-filtered: targets resolving to private,
        loopback, or link-local addresses are rejected. The `target` is write-only —
        it's masked on every read. Requires the `alerts:write` scope (owner/admin only).

        Args:
          target: Destination secret. URL for the webhook flavors (slack/discord/teams/webhook),
              email address for `email`, integration key for `pagerduty`, API key for
              `opsgenie`. URL-bearing types are SSRF-filtered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alert-channels",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target": target,
                    "type": type,
                    "config": config,
                },
                alert_channel_create_params.AlertChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
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
    ) -> AlertChannel:
        """Returns the alert channel.

        The `target` secret is masked. 404 if no such channel
        exists for the calling account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/alert-channels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
        )

    async def update(
        self,
        id: str,
        *,
        config: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        target: str | Omit = omit,
        type: Literal["slack", "discord", "teams", "webhook", "pagerduty", "opsgenie", "email"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannel:
        """All fields are optional; omitted fields are unchanged.

        A `target` equal to the
        masked value (`***<last4>`) is a no-op — only a fresh, non-masked secret updates
        the stored target. Requires the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/alert-channels/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "target": target,
                    "type": type,
                },
                alert_channel_update_params.AlertChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannel,
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
    ) -> AsyncPaginator[AlertChannel, AsyncAlertChannelsCursor[AlertChannel]]:
        """
        Returns the caller's reusable alert channels with cursor pagination.
        `next_cursor` is set when a full page was returned and null on the final page.
        The `target` secret is always masked (`***<last4>`); the raw value is never
        returned. Requires the `alerts:read` scope.

        Args:
          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/alert-channels",
            page=AsyncAlertChannelsCursor[AlertChannel],
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
                    alert_channel_list_params.AlertChannelListParams,
                ),
            ),
            model=AlertChannel,
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
        Deletes the channel and cascades its subscriptions (the bound checks simply stop
        notifying it). Requires the `alerts:write` scope (owner/admin only).

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
            path_template("/v1/alert-channels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test_fire(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertChannelTestFireResponse:
        """
        Enqueues a single `test_fire` dispatch through the channel so a customer can
        verify the destination works. Idempotent on the channel id (repeated clicks
        dedup). Requires the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/alert-channels/{id}:test", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertChannelTestFireResponse,
        )


class AlertChannelsResourceWithRawResponse:
    def __init__(self, alert_channels: AlertChannelsResource) -> None:
        self._alert_channels = alert_channels

        self.create = to_raw_response_wrapper(
            alert_channels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            alert_channels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            alert_channels.update,
        )
        self.list = to_raw_response_wrapper(
            alert_channels.list,
        )
        self.delete = to_raw_response_wrapper(
            alert_channels.delete,
        )
        self.test_fire = to_raw_response_wrapper(
            alert_channels.test_fire,
        )


class AsyncAlertChannelsResourceWithRawResponse:
    def __init__(self, alert_channels: AsyncAlertChannelsResource) -> None:
        self._alert_channels = alert_channels

        self.create = async_to_raw_response_wrapper(
            alert_channels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            alert_channels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            alert_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            alert_channels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            alert_channels.delete,
        )
        self.test_fire = async_to_raw_response_wrapper(
            alert_channels.test_fire,
        )


class AlertChannelsResourceWithStreamingResponse:
    def __init__(self, alert_channels: AlertChannelsResource) -> None:
        self._alert_channels = alert_channels

        self.create = to_streamed_response_wrapper(
            alert_channels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            alert_channels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            alert_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            alert_channels.list,
        )
        self.delete = to_streamed_response_wrapper(
            alert_channels.delete,
        )
        self.test_fire = to_streamed_response_wrapper(
            alert_channels.test_fire,
        )


class AsyncAlertChannelsResourceWithStreamingResponse:
    def __init__(self, alert_channels: AsyncAlertChannelsResource) -> None:
        self._alert_channels = alert_channels

        self.create = async_to_streamed_response_wrapper(
            alert_channels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            alert_channels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            alert_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            alert_channels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            alert_channels.delete,
        )
        self.test_fire = async_to_streamed_response_wrapper(
            alert_channels.test_fire,
        )
