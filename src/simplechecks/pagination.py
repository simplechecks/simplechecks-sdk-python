# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncOffset",
    "AsyncOffset",
    "SyncIncidentsOffset",
    "AsyncIncidentsOffset",
    "SyncRunsCursor",
    "AsyncRunsCursor",
    "SyncAlertChannelsCursor",
    "AsyncAlertChannelsCursor",
    "SyncAlertSubscriptionsCursor",
    "AsyncAlertSubscriptionsCursor",
    "SyncMaintenanceWindowsCursor",
    "AsyncMaintenanceWindowsCursor",
]

_T = TypeVar("_T")


class SyncOffset(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    checks: List[_T]
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        checks = self.checks
        if not checks:
            return []
        return checks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})


class AsyncOffset(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    checks: List[_T]
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        checks = self.checks
        if not checks:
            return []
        return checks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})


class SyncIncidentsOffset(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    incidents: List[_T]
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        incidents = self.incidents
        if not incidents:
            return []
        return incidents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})


class AsyncIncidentsOffset(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    incidents: List[_T]
    next_offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        incidents = self.incidents
        if not incidents:
            return []
        return incidents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})


class SyncRunsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    runs: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runs = self.runs
        if not runs:
            return []
        return runs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncRunsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    runs: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runs = self.runs
        if not runs:
            return []
        return runs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncAlertChannelsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    alert_channels: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        alert_channels = self.alert_channels
        if not alert_channels:
            return []
        return alert_channels

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncAlertChannelsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    alert_channels: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        alert_channels = self.alert_channels
        if not alert_channels:
            return []
        return alert_channels

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncAlertSubscriptionsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    alert_subscriptions: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        alert_subscriptions = self.alert_subscriptions
        if not alert_subscriptions:
            return []
        return alert_subscriptions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncAlertSubscriptionsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    alert_subscriptions: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        alert_subscriptions = self.alert_subscriptions
        if not alert_subscriptions:
            return []
        return alert_subscriptions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncMaintenanceWindowsCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    maintenance_windows: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        maintenance_windows = self.maintenance_windows
        if not maintenance_windows:
            return []
        return maintenance_windows

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncMaintenanceWindowsCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    maintenance_windows: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        maintenance_windows = self.maintenance_windows
        if not maintenance_windows:
            return []
        return maintenance_windows

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
