# Account

Types:

```python
from simplechecks.types import Account
```

Methods:

- <code title="get /v1/account">client.account.<a href="./src/simplechecks/resources/account.py">retrieve</a>() -> <a href="./src/simplechecks/types/account.py">Account</a></code>

# Checks

Types:

```python
from simplechecks.types import AlertConfig, Check
```

Methods:

- <code title="post /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">create</a>(\*\*<a href="src/simplechecks/types/check_create_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="patch /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">update</a>(id, \*\*<a href="src/simplechecks/types/check_update_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">list</a>(\*\*<a href="src/simplechecks/types/check_list_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">SyncOffset[Check]</a></code>
- <code title="delete /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">delete</a>(id) -> None</code>

## Alerts

Methods:

- <code title="get /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/alert_config.py">AlertConfig</a></code>
- <code title="delete /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">delete</a>(id) -> None</code>
- <code title="put /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">replace</a>(id, \*\*<a href="src/simplechecks/types/checks/alert_replace_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_config.py">AlertConfig</a></code>

# Runs

Types:

```python
from simplechecks.types import (
    Aggregate,
    RunDetail,
    RunListItem,
    RunAggregatesResponse,
    RunLogsResponse,
)
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/simplechecks/resources/runs.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/run_detail.py">RunDetail</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/simplechecks/resources/runs.py">list</a>(\*\*<a href="src/simplechecks/types/run_list_params.py">params</a>) -> <a href="./src/simplechecks/types/run_list_item.py">SyncRunsCursor[RunListItem]</a></code>
- <code title="get /v1/runs/aggregates">client.runs.<a href="./src/simplechecks/resources/runs.py">aggregates</a>(\*\*<a href="src/simplechecks/types/run_aggregates_params.py">params</a>) -> <a href="./src/simplechecks/types/run_aggregates_response.py">RunAggregatesResponse</a></code>
- <code title="get /v1/runs/{id}/logs">client.runs.<a href="./src/simplechecks/resources/runs.py">logs</a>(id) -> JSONLDecoder[RunLogsResponse]</code>

# Incidents

Types:

```python
from simplechecks.types import Incident, IncidentListResponse
```

Methods:

- <code title="get /v1/incidents">client.incidents.<a href="./src/simplechecks/resources/incidents.py">list</a>(\*\*<a href="src/simplechecks/types/incident_list_params.py">params</a>) -> <a href="./src/simplechecks/types/incident_list_response.py">IncidentListResponse</a></code>

# Keys

Types:

```python
from simplechecks.types import APIKey, KeyCreateResponse, KeyListResponse
```

Methods:

- <code title="post /v1/keys">client.keys.<a href="./src/simplechecks/resources/keys.py">create</a>(\*\*<a href="src/simplechecks/types/key_create_params.py">params</a>) -> <a href="./src/simplechecks/types/key_create_response.py">KeyCreateResponse</a></code>
- <code title="get /v1/keys">client.keys.<a href="./src/simplechecks/resources/keys.py">list</a>() -> <a href="./src/simplechecks/types/key_list_response.py">KeyListResponse</a></code>
- <code title="delete /v1/keys/{id}">client.keys.<a href="./src/simplechecks/resources/keys.py">revoke</a>(id) -> None</code>

# AlertChannels

Types:

```python
from simplechecks.types import AlertChannel, AlertChannelTestFireResponse
```

Methods:

- <code title="post /v1/alert-channels">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">create</a>(\*\*<a href="src/simplechecks/types/alert_channel_create_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_channel.py">AlertChannel</a></code>
- <code title="get /v1/alert-channels/{id}">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/alert_channel.py">AlertChannel</a></code>
- <code title="patch /v1/alert-channels/{id}">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">update</a>(id, \*\*<a href="src/simplechecks/types/alert_channel_update_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_channel.py">AlertChannel</a></code>
- <code title="get /v1/alert-channels">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">list</a>(\*\*<a href="src/simplechecks/types/alert_channel_list_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_channel.py">SyncAlertChannelsCursor[AlertChannel]</a></code>
- <code title="delete /v1/alert-channels/{id}">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">delete</a>(id) -> None</code>
- <code title="post /v1/alert-channels/{id}:test">client.alert_channels.<a href="./src/simplechecks/resources/alert_channels.py">test_fire</a>(id) -> <a href="./src/simplechecks/types/alert_channel_test_fire_response.py">AlertChannelTestFireResponse</a></code>

# AlertSubscriptions

Types:

```python
from simplechecks.types import AlertSubscription
```

Methods:

- <code title="post /v1/alert-subscriptions">client.alert_subscriptions.<a href="./src/simplechecks/resources/alert_subscriptions.py">create</a>(\*\*<a href="src/simplechecks/types/alert_subscription_create_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_subscription.py">AlertSubscription</a></code>
- <code title="get /v1/alert-subscriptions/{id}">client.alert_subscriptions.<a href="./src/simplechecks/resources/alert_subscriptions.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/alert_subscription.py">AlertSubscription</a></code>
- <code title="patch /v1/alert-subscriptions/{id}">client.alert_subscriptions.<a href="./src/simplechecks/resources/alert_subscriptions.py">update</a>(id, \*\*<a href="src/simplechecks/types/alert_subscription_update_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_subscription.py">AlertSubscription</a></code>
- <code title="get /v1/alert-subscriptions">client.alert_subscriptions.<a href="./src/simplechecks/resources/alert_subscriptions.py">list</a>(\*\*<a href="src/simplechecks/types/alert_subscription_list_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_subscription.py">SyncAlertSubscriptionsCursor[AlertSubscription]</a></code>
- <code title="delete /v1/alert-subscriptions/{id}">client.alert_subscriptions.<a href="./src/simplechecks/resources/alert_subscriptions.py">delete</a>(id) -> None</code>

# MaintenanceWindows

Types:

```python
from simplechecks.types import MaintenanceWindow
```

Methods:

- <code title="post /v1/maintenance-windows">client.maintenance_windows.<a href="./src/simplechecks/resources/maintenance_windows.py">create</a>(\*\*<a href="src/simplechecks/types/maintenance_window_create_params.py">params</a>) -> <a href="./src/simplechecks/types/maintenance_window.py">MaintenanceWindow</a></code>
- <code title="get /v1/maintenance-windows/{id}">client.maintenance_windows.<a href="./src/simplechecks/resources/maintenance_windows.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/maintenance_window.py">MaintenanceWindow</a></code>
- <code title="patch /v1/maintenance-windows/{id}">client.maintenance_windows.<a href="./src/simplechecks/resources/maintenance_windows.py">update</a>(id, \*\*<a href="src/simplechecks/types/maintenance_window_update_params.py">params</a>) -> <a href="./src/simplechecks/types/maintenance_window.py">MaintenanceWindow</a></code>
- <code title="get /v1/maintenance-windows">client.maintenance_windows.<a href="./src/simplechecks/resources/maintenance_windows.py">list</a>(\*\*<a href="src/simplechecks/types/maintenance_window_list_params.py">params</a>) -> <a href="./src/simplechecks/types/maintenance_window.py">SyncMaintenanceWindowsCursor[MaintenanceWindow]</a></code>
- <code title="delete /v1/maintenance-windows/{id}">client.maintenance_windows.<a href="./src/simplechecks/resources/maintenance_windows.py">delete</a>(id) -> None</code>

# Balance

Types:

```python
from simplechecks.types import Balance
```

Methods:

- <code title="get /v1/balance">client.balance.<a href="./src/simplechecks/resources/balance.py">retrieve</a>() -> <a href="./src/simplechecks/types/balance.py">Balance</a></code>

# CheckoutSessions

Types:

```python
from simplechecks.types import CheckoutSession
```

Methods:

- <code title="post /v1/checkout-session">client.checkout_sessions.<a href="./src/simplechecks/resources/checkout_sessions.py">create</a>(\*\*<a href="src/simplechecks/types/checkout_session_create_params.py">params</a>) -> <a href="./src/simplechecks/types/checkout_session.py">CheckoutSession</a></code>

# Purchases

Types:

```python
from simplechecks.types import Purchase, PurchaseListResponse
```

Methods:

- <code title="get /v1/purchases">client.purchases.<a href="./src/simplechecks/resources/purchases.py">list</a>(\*\*<a href="src/simplechecks/types/purchase_list_params.py">params</a>) -> <a href="./src/simplechecks/types/purchase_list_response.py">PurchaseListResponse</a></code>

# Members

Types:

```python
from simplechecks.types import Invitation, Member, MemberListResponse
```

Methods:

- <code title="patch /v1/members/{user_id}">client.members.<a href="./src/simplechecks/resources/members/members.py">update</a>(user_id, \*\*<a href="src/simplechecks/types/member_update_params.py">params</a>) -> <a href="./src/simplechecks/types/member.py">Member</a></code>
- <code title="get /v1/members">client.members.<a href="./src/simplechecks/resources/members/members.py">list</a>() -> <a href="./src/simplechecks/types/member_list_response.py">MemberListResponse</a></code>
- <code title="delete /v1/members/{user_id}">client.members.<a href="./src/simplechecks/resources/members/members.py">remove</a>(user_id) -> None</code>

## Invitations

Types:

```python
from simplechecks.types.members import InvitationListResponse
```

Methods:

- <code title="post /v1/invitations">client.members.invitations.<a href="./src/simplechecks/resources/members/invitations.py">create</a>(\*\*<a href="src/simplechecks/types/members/invitation_create_params.py">params</a>) -> <a href="./src/simplechecks/types/invitation.py">Invitation</a></code>
- <code title="get /v1/invitations">client.members.invitations.<a href="./src/simplechecks/resources/members/invitations.py">list</a>() -> <a href="./src/simplechecks/types/members/invitation_list_response.py">InvitationListResponse</a></code>
- <code title="delete /v1/invitations/{id}">client.members.invitations.<a href="./src/simplechecks/resources/members/invitations.py">revoke</a>(id) -> None</code>

# Locations

Types:

```python
from simplechecks.types import Location, LocationListResponse
```

Methods:

- <code title="get /v1/locations">client.locations.<a href="./src/simplechecks/resources/locations.py">list</a>() -> <a href="./src/simplechecks/types/location_list_response.py">LocationListResponse</a></code>

# Pricing

Types:

```python
from simplechecks.types import Pricing
```

Methods:

- <code title="get /v1/pricing">client.pricing.<a href="./src/simplechecks/resources/pricing.py">retrieve</a>() -> <a href="./src/simplechecks/types/pricing.py">Pricing</a></code>
