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
from simplechecks.types import AlertChannel, AlertConfig, Check, MaintenanceWindow
```

Methods:

- <code title="post /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">create</a>(\*\*<a href="src/simplechecks/types/check_create_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="patch /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">update</a>(id, \*\*<a href="src/simplechecks/types/check_update_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">list</a>(\*\*<a href="src/simplechecks/types/check_list_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">SyncOffset[Check]</a></code>
- <code title="delete /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks/checks.py">delete</a>(id) -> None</code>

## Alerts

Types:

```python
from simplechecks.types.checks import AlertTestFireResponse
```

Methods:

- <code title="get /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/alert_config.py">AlertConfig</a></code>
- <code title="delete /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">delete</a>(id) -> None</code>
- <code title="put /v1/checks/{id}/alerts">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">replace</a>(id, \*\*<a href="src/simplechecks/types/checks/alert_replace_params.py">params</a>) -> <a href="./src/simplechecks/types/alert_config.py">AlertConfig</a></code>
- <code title="post /v1/checks/{id}/alerts:test">client.checks.alerts.<a href="./src/simplechecks/resources/checks/alerts.py">test_fire</a>(id) -> <a href="./src/simplechecks/types/checks/alert_test_fire_response.py">AlertTestFireResponse</a></code>

# Runs

Types:

```python
from simplechecks.types import (
    Aggregate,
    Run,
    RunListResponse,
    RunAggregatesResponse,
    RunLogsResponse,
)
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/simplechecks/resources/runs.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/run.py">Run</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/simplechecks/resources/runs.py">list</a>(\*\*<a href="src/simplechecks/types/run_list_params.py">params</a>) -> <a href="./src/simplechecks/types/run_list_response.py">RunListResponse</a></code>
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
