# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import alert_subscription_list_params, alert_subscription_create_params, alert_subscription_update_params
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
from ..pagination import SyncAlertSubscriptionsCursor, AsyncAlertSubscriptionsCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.alert_subscription import AlertSubscription

__all__ = ["AlertSubscriptionsResource", "AsyncAlertSubscriptionsResource"]


class AlertSubscriptionsResource(SyncAPIResource):
    """
    Bindings of a check to an alert channel, each carrying its own
    notify-on-failure / notify-on-recovery flags.
    """

    @cached_property
    def with_raw_response(self) -> AlertSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlertSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AlertSubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        channel_id: str,
        check_id: str,
        notify_on_failure: bool | Omit = omit,
        notify_on_recovery: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertSubscription:
        """
        Binds a check to a channel and carries the per-binding notify flags
        (`notify_on_failure`, `notify_on_recovery`, both default true). The binding is
        account-scoped: a check or channel that isn't yours yields 404. A duplicate
        `(check_id, channel_id)` binding yields 409. Requires the `alerts:write` scope
        (owner/admin only).

        Args:
          channel_id: The channel to bind in `chan_<typeid>` form (must belong to your account).

          check_id: The check to subscribe (must belong to your account).

          notify_on_failure: Defaults to true when omitted.

          notify_on_recovery: Defaults to true when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alert-subscriptions",
            body=maybe_transform(
                {
                    "channel_id": channel_id,
                    "check_id": check_id,
                    "notify_on_failure": notify_on_failure,
                    "notify_on_recovery": notify_on_recovery,
                },
                alert_subscription_create_params.AlertSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
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
    ) -> AlertSubscription:
        """Returns the subscription.

        404 if no such subscription exists for the calling
        account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/alert-subscriptions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
        )

    def update(
        self,
        id: str,
        *,
        notify_on_failure: bool | Omit = omit,
        notify_on_recovery: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertSubscription:
        """
        Updates only the notify flags (`notify_on_failure`, `notify_on_recovery`); the
        check and channel bindings are immutable. Omitted flags are unchanged. Requires
        the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/alert-subscriptions/{id}", id=id),
            body=maybe_transform(
                {
                    "notify_on_failure": notify_on_failure,
                    "notify_on_recovery": notify_on_recovery,
                },
                alert_subscription_update_params.AlertSubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
        )

    def list(
        self,
        *,
        channel_id: str | Omit = omit,
        check_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncAlertSubscriptionsCursor[AlertSubscription]:
        """
        Returns the caller's check↔channel subscriptions with cursor pagination.
        Optionally filter by `check_id` and/or `channel_id`. `next_cursor` is set when a
        full page was returned and null on the final page. Requires the `alerts:read`
        scope.

        Args:
          channel_id: Filter to subscriptions for this channel (`chan_<typeid>`).

          check_id: Filter to subscriptions for this check (raw check UUID).

          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/alert-subscriptions",
            page=SyncAlertSubscriptionsCursor[AlertSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel_id": channel_id,
                        "check_id": check_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    alert_subscription_list_params.AlertSubscriptionListParams,
                ),
            ),
            model=AlertSubscription,
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
        """Removes the binding; the check stops notifying that channel.

        Requires the
        `alerts:write` scope (owner/admin only).

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
            path_template("/v1/alert-subscriptions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAlertSubscriptionsResource(AsyncAPIResource):
    """
    Bindings of a check to an alert channel, each carrying its own
    notify-on-failure / notify-on-recovery flags.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAlertSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncAlertSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        channel_id: str,
        check_id: str,
        notify_on_failure: bool | Omit = omit,
        notify_on_recovery: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertSubscription:
        """
        Binds a check to a channel and carries the per-binding notify flags
        (`notify_on_failure`, `notify_on_recovery`, both default true). The binding is
        account-scoped: a check or channel that isn't yours yields 404. A duplicate
        `(check_id, channel_id)` binding yields 409. Requires the `alerts:write` scope
        (owner/admin only).

        Args:
          channel_id: The channel to bind in `chan_<typeid>` form (must belong to your account).

          check_id: The check to subscribe (must belong to your account).

          notify_on_failure: Defaults to true when omitted.

          notify_on_recovery: Defaults to true when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alert-subscriptions",
            body=await async_maybe_transform(
                {
                    "channel_id": channel_id,
                    "check_id": check_id,
                    "notify_on_failure": notify_on_failure,
                    "notify_on_recovery": notify_on_recovery,
                },
                alert_subscription_create_params.AlertSubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
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
    ) -> AlertSubscription:
        """Returns the subscription.

        404 if no such subscription exists for the calling
        account. Requires the `alerts:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/alert-subscriptions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
        )

    async def update(
        self,
        id: str,
        *,
        notify_on_failure: bool | Omit = omit,
        notify_on_recovery: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertSubscription:
        """
        Updates only the notify flags (`notify_on_failure`, `notify_on_recovery`); the
        check and channel bindings are immutable. Omitted flags are unchanged. Requires
        the `alerts:write` scope (owner/admin only).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/alert-subscriptions/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "notify_on_failure": notify_on_failure,
                    "notify_on_recovery": notify_on_recovery,
                },
                alert_subscription_update_params.AlertSubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertSubscription,
        )

    def list(
        self,
        *,
        channel_id: str | Omit = omit,
        check_id: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AlertSubscription, AsyncAlertSubscriptionsCursor[AlertSubscription]]:
        """
        Returns the caller's check↔channel subscriptions with cursor pagination.
        Optionally filter by `check_id` and/or `channel_id`. `next_cursor` is set when a
        full page was returned and null on the final page. Requires the `alerts:read`
        scope.

        Args:
          channel_id: Filter to subscriptions for this channel (`chan_<typeid>`).

          check_id: Filter to subscriptions for this check (raw check UUID).

          cursor: Opaque pagination token from the previous page's `next_cursor`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/alert-subscriptions",
            page=AsyncAlertSubscriptionsCursor[AlertSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel_id": channel_id,
                        "check_id": check_id,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    alert_subscription_list_params.AlertSubscriptionListParams,
                ),
            ),
            model=AlertSubscription,
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
        """Removes the binding; the check stops notifying that channel.

        Requires the
        `alerts:write` scope (owner/admin only).

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
            path_template("/v1/alert-subscriptions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AlertSubscriptionsResourceWithRawResponse:
    def __init__(self, alert_subscriptions: AlertSubscriptionsResource) -> None:
        self._alert_subscriptions = alert_subscriptions

        self.create = to_raw_response_wrapper(
            alert_subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            alert_subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            alert_subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            alert_subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            alert_subscriptions.delete,
        )


class AsyncAlertSubscriptionsResourceWithRawResponse:
    def __init__(self, alert_subscriptions: AsyncAlertSubscriptionsResource) -> None:
        self._alert_subscriptions = alert_subscriptions

        self.create = async_to_raw_response_wrapper(
            alert_subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            alert_subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            alert_subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            alert_subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            alert_subscriptions.delete,
        )


class AlertSubscriptionsResourceWithStreamingResponse:
    def __init__(self, alert_subscriptions: AlertSubscriptionsResource) -> None:
        self._alert_subscriptions = alert_subscriptions

        self.create = to_streamed_response_wrapper(
            alert_subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            alert_subscriptions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            alert_subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            alert_subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            alert_subscriptions.delete,
        )


class AsyncAlertSubscriptionsResourceWithStreamingResponse:
    def __init__(self, alert_subscriptions: AsyncAlertSubscriptionsResource) -> None:
        self._alert_subscriptions = alert_subscriptions

        self.create = async_to_streamed_response_wrapper(
            alert_subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            alert_subscriptions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            alert_subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            alert_subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            alert_subscriptions.delete,
        )
