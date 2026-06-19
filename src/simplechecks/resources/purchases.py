# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import purchase_list_params
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
from ..types.purchase_list_response import PurchaseListResponse

__all__ = ["PurchasesResource", "AsyncPurchasesResource"]


class PurchasesResource(SyncAPIResource):
    """Run-credit balance, Stripe Checkout top-ups, and purchase history."""

    @cached_property
    def with_raw_response(self) -> PurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return PurchasesResourceWithStreamingResponse(self)

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
    ) -> PurchaseListResponse:
        """
        Returns every Stripe Checkout bundle purchase for the caller's account, newest
        first. Powers the "Invoices" section of Settings → Billing in the webapp. The
        `receipt_url`, when present, links to the Stripe-hosted receipt PDF. Reading
        purchase history requires only the default-scope `account:read` — spending money
        on a new purchase requires the opt-in `billing:write` scope (POST
        /v1/checkout-session).

        Args:
          limit: Page size. Server applies a default of 100 when omitted or when set to 0; values
              above the server cap are clamped.

          offset: Pagination offset within the newest-first list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/purchases",
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
                    purchase_list_params.PurchaseListParams,
                ),
            ),
            cast_to=PurchaseListResponse,
        )


class AsyncPurchasesResource(AsyncAPIResource):
    """Run-credit balance, Stripe Checkout top-ups, and purchase history."""

    @cached_property
    def with_raw_response(self) -> AsyncPurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncPurchasesResourceWithStreamingResponse(self)

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
    ) -> PurchaseListResponse:
        """
        Returns every Stripe Checkout bundle purchase for the caller's account, newest
        first. Powers the "Invoices" section of Settings → Billing in the webapp. The
        `receipt_url`, when present, links to the Stripe-hosted receipt PDF. Reading
        purchase history requires only the default-scope `account:read` — spending money
        on a new purchase requires the opt-in `billing:write` scope (POST
        /v1/checkout-session).

        Args:
          limit: Page size. Server applies a default of 100 when omitted or when set to 0; values
              above the server cap are clamped.

          offset: Pagination offset within the newest-first list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/purchases",
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
                    purchase_list_params.PurchaseListParams,
                ),
            ),
            cast_to=PurchaseListResponse,
        )


class PurchasesResourceWithRawResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.list = to_raw_response_wrapper(
            purchases.list,
        )


class AsyncPurchasesResourceWithRawResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.list = async_to_raw_response_wrapper(
            purchases.list,
        )


class PurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.list = to_streamed_response_wrapper(
            purchases.list,
        )


class AsyncPurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.list = async_to_streamed_response_wrapper(
            purchases.list,
        )
