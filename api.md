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
from simplechecks.types import Check
```

Methods:

- <code title="delete /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks.py">delete</a>(id) -> None</code>

# Runs

Types:

```python
from simplechecks.types import Run, RunListResponse
```

Methods:

- <code title="get /v1/runs/{id}">client.runs.<a href="./src/simplechecks/resources/runs.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/run.py">Run</a></code>
- <code title="get /v1/runs">client.runs.<a href="./src/simplechecks/resources/runs.py">list</a>(\*\*<a href="src/simplechecks/types/run_list_params.py">params</a>) -> <a href="./src/simplechecks/types/run_list_response.py">RunListResponse</a></code>

# Keys

Types:

```python
from simplechecks.types import APIKey
```

Methods:

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
