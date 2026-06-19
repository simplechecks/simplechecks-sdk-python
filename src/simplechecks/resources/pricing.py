# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.pricing import Pricing

__all__ = ["PricingResource", "AsyncPricingResource"]


class PricingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return PricingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pricing:
        """
        Returns the active token-pricing table so a client can show the per-provider
        cost of a check at configuration time. The cost of one run is
        `floor(weight × multiplier_milli / 1000)`, where `weight` is the check type's
        compute weight plus its artifact-egress component, and the multiplier resolves
        `(provider, location)` → `(provider, "")` → `1.0` (returned as `1000` milli).
        The result equals what metering debits, so a UI preview is exact.

        The provider multiplier is the customer-facing cost lever: cheaper providers
        (e.g. OVH, Hetzner) carry a multiplier below 1.0. Reads of this table are free.

        Requires the `account:read` scope — pricing is incidental to account/check
        configuration, not a per-check write.
        """
        return self._get(
            "/v1/pricing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pricing,
        )


class AsyncPricingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/simplechecks/simplechecks-sdk-python#with_streaming_response
        """
        return AsyncPricingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pricing:
        """
        Returns the active token-pricing table so a client can show the per-provider
        cost of a check at configuration time. The cost of one run is
        `floor(weight × multiplier_milli / 1000)`, where `weight` is the check type's
        compute weight plus its artifact-egress component, and the multiplier resolves
        `(provider, location)` → `(provider, "")` → `1.0` (returned as `1000` milli).
        The result equals what metering debits, so a UI preview is exact.

        The provider multiplier is the customer-facing cost lever: cheaper providers
        (e.g. OVH, Hetzner) carry a multiplier below 1.0. Reads of this table are free.

        Requires the `account:read` scope — pricing is incidental to account/check
        configuration, not a per-check write.
        """
        return await self._get(
            "/v1/pricing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pricing,
        )


class PricingResourceWithRawResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

        self.retrieve = to_raw_response_wrapper(
            pricing.retrieve,
        )


class AsyncPricingResourceWithRawResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

        self.retrieve = async_to_raw_response_wrapper(
            pricing.retrieve,
        )


class PricingResourceWithStreamingResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

        self.retrieve = to_streamed_response_wrapper(
            pricing.retrieve,
        )


class AsyncPricingResourceWithStreamingResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

        self.retrieve = async_to_streamed_response_wrapper(
            pricing.retrieve,
        )
