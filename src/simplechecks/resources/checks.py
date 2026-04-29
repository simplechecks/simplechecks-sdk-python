# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import check_list_params, check_create_params, check_update_params
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
from ..types.check import Check
from .._base_client import make_request_options
from ..types.check_list_response import CheckListResponse

__all__ = ["ChecksResource", "AsyncChecksResource"]


class ChecksResource(SyncAPIResource):
    """CRUD for synthetic-monitoring checks."""

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

    def create(
        self,
        *,
        enabled: bool,
        location: str,
        name: str,
        provider: str,
        schedule: str,
        target_url: str,
        type: str,
        artifact_url: str | Omit = omit,
        config: Dict[str, object] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """
        Creates a check bound to the resolved garrison for the given `provider` +
        `location`. Requires the `checks:write` scope.

        Args:
          location: Provider-specific region/location.

          provider: Cloud provider (`mock`, `ec2`, `ovh`, `azure`, `gcp`, `hetzner`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/checks",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "location": location,
                    "name": name,
                    "provider": provider,
                    "schedule": schedule,
                    "target_url": target_url,
                    "type": type,
                    "artifact_url": artifact_url,
                    "config": config,
                    "timeout_ms": timeout_ms,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
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
    ) -> Check:
        """Returns the check with the given id.

        404 if no such check exists for the calling
        account. Requires the `checks:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
        )

    def update(
        self,
        id: str,
        *,
        artifact_url: str | Omit = omit,
        config: Dict[str, object] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        schedule: str | Omit = omit,
        target_url: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """All fields in the body are optional; omitted fields are left unchanged.

        Requires
        the `checks:write` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/checks/{id}", id=id),
            body=maybe_transform(
                {
                    "artifact_url": artifact_url,
                    "config": config,
                    "enabled": enabled,
                    "name": name,
                    "schedule": schedule,
                    "target_url": target_url,
                    "timeout_ms": timeout_ms,
                    "type": type,
                },
                check_update_params.CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
        )

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
    ) -> CheckListResponse:
        """Returns the caller's checks with simple offset pagination.

        `next_offset` is set
        when a full page was returned and zero when there's no more data. Requires the
        `checks:read` scope.

        Args:
          limit: Max number of checks to return. Defaults to 100; the server caps further.

          offset: Number of checks to skip. Pass the `next_offset` from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/checks",
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
                    check_list_params.CheckListParams,
                ),
            ),
            cast_to=CheckListResponse,
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

    async def create(
        self,
        *,
        enabled: bool,
        location: str,
        name: str,
        provider: str,
        schedule: str,
        target_url: str,
        type: str,
        artifact_url: str | Omit = omit,
        config: Dict[str, object] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """
        Creates a check bound to the resolved garrison for the given `provider` +
        `location`. Requires the `checks:write` scope.

        Args:
          location: Provider-specific region/location.

          provider: Cloud provider (`mock`, `ec2`, `ovh`, `azure`, `gcp`, `hetzner`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/checks",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "location": location,
                    "name": name,
                    "provider": provider,
                    "schedule": schedule,
                    "target_url": target_url,
                    "type": type,
                    "artifact_url": artifact_url,
                    "config": config,
                    "timeout_ms": timeout_ms,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
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
    ) -> Check:
        """Returns the check with the given id.

        404 if no such check exists for the calling
        account. Requires the `checks:read` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/checks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
        )

    async def update(
        self,
        id: str,
        *,
        artifact_url: str | Omit = omit,
        config: Dict[str, object] | Omit = omit,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        schedule: str | Omit = omit,
        target_url: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """All fields in the body are optional; omitted fields are left unchanged.

        Requires
        the `checks:write` scope.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/checks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "artifact_url": artifact_url,
                    "config": config,
                    "enabled": enabled,
                    "name": name,
                    "schedule": schedule,
                    "target_url": target_url,
                    "timeout_ms": timeout_ms,
                    "type": type,
                },
                check_update_params.CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Check,
        )

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
    ) -> CheckListResponse:
        """Returns the caller's checks with simple offset pagination.

        `next_offset` is set
        when a full page was returned and zero when there's no more data. Requires the
        `checks:read` scope.

        Args:
          limit: Max number of checks to return. Defaults to 100; the server caps further.

          offset: Number of checks to skip. Pass the `next_offset` from the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/checks",
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
                    check_list_params.CheckListParams,
                ),
            ),
            cast_to=CheckListResponse,
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

        self.create = to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            checks.update,
        )
        self.list = to_raw_response_wrapper(
            checks.list,
        )
        self.delete = to_raw_response_wrapper(
            checks.delete,
        )


class AsyncChecksResourceWithRawResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            checks.update,
        )
        self.list = async_to_raw_response_wrapper(
            checks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            checks.delete,
        )


class ChecksResourceWithStreamingResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.create = to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            checks.update,
        )
        self.list = to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = to_streamed_response_wrapper(
            checks.delete,
        )


class AsyncChecksResourceWithStreamingResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            checks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            checks.delete,
        )
