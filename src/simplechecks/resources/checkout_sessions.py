# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import checkout_session_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.checkout_session import CheckoutSession

__all__ = ["CheckoutSessionsResource", "AsyncCheckoutSessionsResource"]


class CheckoutSessionsResource(SyncAPIResource):
    """Run-credit balance + Stripe Checkout for top-ups."""

    @cached_property
    def with_raw_response(self) -> CheckoutSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return CheckoutSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bundle_sku: Literal["starter", "growth", "scale", "team"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutSession:
        """Returns a Stripe-hosted checkout URL the customer pays on.

        The webhook fulfils
        the purchase asynchronously after the customer completes payment. Requires the
        `billing:write` scope (opt-in; not in the default scope set, since spending
        money should be a deliberate choice).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/checkout-session",
            body=maybe_transform(
                {"bundle_sku": bundle_sku}, checkout_session_create_params.CheckoutSessionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutSession,
        )


class AsyncCheckoutSessionsResource(AsyncAPIResource):
    """Run-credit balance + Stripe Checkout for top-ups."""

    @cached_property
    def with_raw_response(self) -> AsyncCheckoutSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncCheckoutSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bundle_sku: Literal["starter", "growth", "scale", "team"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutSession:
        """Returns a Stripe-hosted checkout URL the customer pays on.

        The webhook fulfils
        the purchase asynchronously after the customer completes payment. Requires the
        `billing:write` scope (opt-in; not in the default scope set, since spending
        money should be a deliberate choice).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/checkout-session",
            body=await async_maybe_transform(
                {"bundle_sku": bundle_sku}, checkout_session_create_params.CheckoutSessionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckoutSession,
        )


class CheckoutSessionsResourceWithRawResponse:
    def __init__(self, checkout_sessions: CheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = to_raw_response_wrapper(
            checkout_sessions.create,
        )


class AsyncCheckoutSessionsResourceWithRawResponse:
    def __init__(self, checkout_sessions: AsyncCheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = async_to_raw_response_wrapper(
            checkout_sessions.create,
        )


class CheckoutSessionsResourceWithStreamingResponse:
    def __init__(self, checkout_sessions: CheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = to_streamed_response_wrapper(
            checkout_sessions.create,
        )


class AsyncCheckoutSessionsResourceWithStreamingResponse:
    def __init__(self, checkout_sessions: AsyncCheckoutSessionsResource) -> None:
        self._checkout_sessions = checkout_sessions

        self.create = async_to_streamed_response_wrapper(
            checkout_sessions.create,
        )
