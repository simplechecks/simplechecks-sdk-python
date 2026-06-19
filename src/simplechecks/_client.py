# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        keys,
        runs,
        checks,
        account,
        balance,
        members,
        pricing,
        incidents,
        locations,
        purchases,
        checkout_sessions,
    )
    from .resources.keys import KeysResource, AsyncKeysResource
    from .resources.runs import RunsResource, AsyncRunsResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.balance import BalanceResource, AsyncBalanceResource
    from .resources.pricing import PricingResource, AsyncPricingResource
    from .resources.incidents import IncidentsResource, AsyncIncidentsResource
    from .resources.locations import LocationsResource, AsyncLocationsResource
    from .resources.purchases import PurchasesResource, AsyncPurchasesResource
    from .resources.checks.checks import ChecksResource, AsyncChecksResource
    from .resources.members.members import MembersResource, AsyncMembersResource
    from .resources.checkout_sessions import CheckoutSessionsResource, AsyncCheckoutSessionsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "SimpleChecks",
    "AsyncSimpleChecks",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.simplechecks.com",
    "local": "http://localhost:8080",
}


class SimpleChecks(SyncAPIClient):
    # client options
    api_key: str | None

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SimpleChecks client instance.

        This automatically infers the `api_key` argument from the `SIMPLECHECKS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SIMPLECHECKS_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("SIMPLE_CHECKS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SIMPLE_CHECKS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("SIMPLE_CHECKS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account(self) -> AccountResource:
        """Account profile and balance."""
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def checks(self) -> ChecksResource:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import ChecksResource

        return ChecksResource(self)

    @cached_property
    def runs(self) -> RunsResource:
        """Read-only access to past check executions."""
        from .resources.runs import RunsResource

        return RunsResource(self)

    @cached_property
    def incidents(self) -> IncidentsResource:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import IncidentsResource

        return IncidentsResource(self)

    @cached_property
    def keys(self) -> KeysResource:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import KeysResource

        return KeysResource(self)

    @cached_property
    def balance(self) -> BalanceResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import BalanceResource

        return BalanceResource(self)

    @cached_property
    def checkout_sessions(self) -> CheckoutSessionsResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import CheckoutSessionsResource

        return CheckoutSessionsResource(self)

    @cached_property
    def purchases(self) -> PurchasesResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import PurchasesResource

        return PurchasesResource(self)

    @cached_property
    def members(self) -> MembersResource:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import MembersResource

        return MembersResource(self)

    @cached_property
    def locations(self) -> LocationsResource:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import LocationsResource

        return LocationsResource(self)

    @cached_property
    def pricing(self) -> PricingResource:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import PricingResource

        return PricingResource(self)

    @cached_property
    def with_raw_response(self) -> SimpleChecksWithRawResponse:
        return SimpleChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimpleChecksWithStreamedResponse:
        return SimpleChecksWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSimpleChecks(AsyncAPIClient):
    # client options
    api_key: str | None

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSimpleChecks client instance.

        This automatically infers the `api_key` argument from the `SIMPLECHECKS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SIMPLECHECKS_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("SIMPLE_CHECKS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `SIMPLE_CHECKS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("SIMPLE_CHECKS_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def account(self) -> AsyncAccountResource:
        """Account profile and balance."""
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def checks(self) -> AsyncChecksResource:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import AsyncChecksResource

        return AsyncChecksResource(self)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        """Read-only access to past check executions."""
        from .resources.runs import AsyncRunsResource

        return AsyncRunsResource(self)

    @cached_property
    def incidents(self) -> AsyncIncidentsResource:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import AsyncIncidentsResource

        return AsyncIncidentsResource(self)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import AsyncKeysResource

        return AsyncKeysResource(self)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import AsyncBalanceResource

        return AsyncBalanceResource(self)

    @cached_property
    def checkout_sessions(self) -> AsyncCheckoutSessionsResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import AsyncCheckoutSessionsResource

        return AsyncCheckoutSessionsResource(self)

    @cached_property
    def purchases(self) -> AsyncPurchasesResource:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import AsyncPurchasesResource

        return AsyncPurchasesResource(self)

    @cached_property
    def members(self) -> AsyncMembersResource:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import AsyncMembersResource

        return AsyncMembersResource(self)

    @cached_property
    def locations(self) -> AsyncLocationsResource:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import AsyncLocationsResource

        return AsyncLocationsResource(self)

    @cached_property
    def pricing(self) -> AsyncPricingResource:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import AsyncPricingResource

        return AsyncPricingResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSimpleChecksWithRawResponse:
        return AsyncSimpleChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimpleChecksWithStreamedResponse:
        return AsyncSimpleChecksWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SimpleChecksWithRawResponse:
    _client: SimpleChecks

    def __init__(self, client: SimpleChecks) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        """Account profile and balance."""
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def checks(self) -> checks.ChecksResourceWithRawResponse:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import ChecksResourceWithRawResponse

        return ChecksResourceWithRawResponse(self._client.checks)

    @cached_property
    def runs(self) -> runs.RunsResourceWithRawResponse:
        """Read-only access to past check executions."""
        from .resources.runs import RunsResourceWithRawResponse

        return RunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def incidents(self) -> incidents.IncidentsResourceWithRawResponse:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import IncidentsResourceWithRawResponse

        return IncidentsResourceWithRawResponse(self._client.incidents)

    @cached_property
    def keys(self) -> keys.KeysResourceWithRawResponse:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import KeysResourceWithRawResponse

        return KeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import BalanceResourceWithRawResponse

        return BalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.CheckoutSessionsResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import CheckoutSessionsResourceWithRawResponse

        return CheckoutSessionsResourceWithRawResponse(self._client.checkout_sessions)

    @cached_property
    def purchases(self) -> purchases.PurchasesResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import PurchasesResourceWithRawResponse

        return PurchasesResourceWithRawResponse(self._client.purchases)

    @cached_property
    def members(self) -> members.MembersResourceWithRawResponse:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import MembersResourceWithRawResponse

        return MembersResourceWithRawResponse(self._client.members)

    @cached_property
    def locations(self) -> locations.LocationsResourceWithRawResponse:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import LocationsResourceWithRawResponse

        return LocationsResourceWithRawResponse(self._client.locations)

    @cached_property
    def pricing(self) -> pricing.PricingResourceWithRawResponse:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import PricingResourceWithRawResponse

        return PricingResourceWithRawResponse(self._client.pricing)


class AsyncSimpleChecksWithRawResponse:
    _client: AsyncSimpleChecks

    def __init__(self, client: AsyncSimpleChecks) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        """Account profile and balance."""
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def checks(self) -> checks.AsyncChecksResourceWithRawResponse:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import AsyncChecksResourceWithRawResponse

        return AsyncChecksResourceWithRawResponse(self._client.checks)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithRawResponse:
        """Read-only access to past check executions."""
        from .resources.runs import AsyncRunsResourceWithRawResponse

        return AsyncRunsResourceWithRawResponse(self._client.runs)

    @cached_property
    def incidents(self) -> incidents.AsyncIncidentsResourceWithRawResponse:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import AsyncIncidentsResourceWithRawResponse

        return AsyncIncidentsResourceWithRawResponse(self._client.incidents)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithRawResponse:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import AsyncKeysResourceWithRawResponse

        return AsyncKeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import AsyncBalanceResourceWithRawResponse

        return AsyncBalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.AsyncCheckoutSessionsResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import AsyncCheckoutSessionsResourceWithRawResponse

        return AsyncCheckoutSessionsResourceWithRawResponse(self._client.checkout_sessions)

    @cached_property
    def purchases(self) -> purchases.AsyncPurchasesResourceWithRawResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import AsyncPurchasesResourceWithRawResponse

        return AsyncPurchasesResourceWithRawResponse(self._client.purchases)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithRawResponse:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import AsyncMembersResourceWithRawResponse

        return AsyncMembersResourceWithRawResponse(self._client.members)

    @cached_property
    def locations(self) -> locations.AsyncLocationsResourceWithRawResponse:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import AsyncLocationsResourceWithRawResponse

        return AsyncLocationsResourceWithRawResponse(self._client.locations)

    @cached_property
    def pricing(self) -> pricing.AsyncPricingResourceWithRawResponse:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import AsyncPricingResourceWithRawResponse

        return AsyncPricingResourceWithRawResponse(self._client.pricing)


class SimpleChecksWithStreamedResponse:
    _client: SimpleChecks

    def __init__(self, client: SimpleChecks) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        """Account profile and balance."""
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def checks(self) -> checks.ChecksResourceWithStreamingResponse:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import ChecksResourceWithStreamingResponse

        return ChecksResourceWithStreamingResponse(self._client.checks)

    @cached_property
    def runs(self) -> runs.RunsResourceWithStreamingResponse:
        """Read-only access to past check executions."""
        from .resources.runs import RunsResourceWithStreamingResponse

        return RunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def incidents(self) -> incidents.IncidentsResourceWithStreamingResponse:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import IncidentsResourceWithStreamingResponse

        return IncidentsResourceWithStreamingResponse(self._client.incidents)

    @cached_property
    def keys(self) -> keys.KeysResourceWithStreamingResponse:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import KeysResourceWithStreamingResponse

        return KeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import BalanceResourceWithStreamingResponse

        return BalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.CheckoutSessionsResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import CheckoutSessionsResourceWithStreamingResponse

        return CheckoutSessionsResourceWithStreamingResponse(self._client.checkout_sessions)

    @cached_property
    def purchases(self) -> purchases.PurchasesResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import PurchasesResourceWithStreamingResponse

        return PurchasesResourceWithStreamingResponse(self._client.purchases)

    @cached_property
    def members(self) -> members.MembersResourceWithStreamingResponse:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import MembersResourceWithStreamingResponse

        return MembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def locations(self) -> locations.LocationsResourceWithStreamingResponse:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import LocationsResourceWithStreamingResponse

        return LocationsResourceWithStreamingResponse(self._client.locations)

    @cached_property
    def pricing(self) -> pricing.PricingResourceWithStreamingResponse:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import PricingResourceWithStreamingResponse

        return PricingResourceWithStreamingResponse(self._client.pricing)


class AsyncSimpleChecksWithStreamedResponse:
    _client: AsyncSimpleChecks

    def __init__(self, client: AsyncSimpleChecks) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        """Account profile and balance."""
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def checks(self) -> checks.AsyncChecksResourceWithStreamingResponse:
        """CRUD for synthetic-monitoring checks."""
        from .resources.checks import AsyncChecksResourceWithStreamingResponse

        return AsyncChecksResourceWithStreamingResponse(self._client.checks)

    @cached_property
    def runs(self) -> runs.AsyncRunsResourceWithStreamingResponse:
        """Read-only access to past check executions."""
        from .resources.runs import AsyncRunsResourceWithStreamingResponse

        return AsyncRunsResourceWithStreamingResponse(self._client.runs)

    @cached_property
    def incidents(self) -> incidents.AsyncIncidentsResourceWithStreamingResponse:
        """Read-only incident timeline derived from alert state."""
        from .resources.incidents import AsyncIncidentsResourceWithStreamingResponse

        return AsyncIncidentsResourceWithStreamingResponse(self._client.incidents)

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithStreamingResponse:
        """Manage personal access tokens (PATs)."""
        from .resources.keys import AsyncKeysResourceWithStreamingResponse

        return AsyncKeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.balance import AsyncBalanceResourceWithStreamingResponse

        return AsyncBalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def checkout_sessions(self) -> checkout_sessions.AsyncCheckoutSessionsResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.checkout_sessions import AsyncCheckoutSessionsResourceWithStreamingResponse

        return AsyncCheckoutSessionsResourceWithStreamingResponse(self._client.checkout_sessions)

    @cached_property
    def purchases(self) -> purchases.AsyncPurchasesResourceWithStreamingResponse:
        """Run-credit balance, Stripe Checkout top-ups, and purchase history."""
        from .resources.purchases import AsyncPurchasesResourceWithStreamingResponse

        return AsyncPurchasesResourceWithStreamingResponse(self._client.purchases)

    @cached_property
    def members(self) -> members.AsyncMembersResourceWithStreamingResponse:
        """Manage who has access to an account and at what role
        (PR-Members/2).

        Five roles: owner / admin / member / billing /
        viewer. Owner is the strict superset of all other roles' scopes;
        every account always has at least one owner.
        """
        from .resources.members import AsyncMembersResourceWithStreamingResponse

        return AsyncMembersResourceWithStreamingResponse(self._client.members)

    @cached_property
    def locations(self) -> locations.AsyncLocationsResourceWithStreamingResponse:
        """
        Catalog of (provider, location) deployments Simple Checks runs
        checks from, with geographic metadata + live status. Used to
        drive the region picker and the dashboard's locations map.
        """
        from .resources.locations import AsyncLocationsResourceWithStreamingResponse

        return AsyncLocationsResourceWithStreamingResponse(self._client.locations)

    @cached_property
    def pricing(self) -> pricing.AsyncPricingResourceWithStreamingResponse:
        """
        Active token-pricing table: per-check-type weights and the
        customer-facing provider cost multipliers. Reads are free.
        """
        from .resources.pricing import AsyncPricingResourceWithStreamingResponse

        return AsyncPricingResourceWithStreamingResponse(self._client.pricing)


Client = SimpleChecks

AsyncClient = AsyncSimpleChecks
