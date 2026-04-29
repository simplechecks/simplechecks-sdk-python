# Healthz

Types:

```python
from simplechecks.types import HealthzCheckResponse
```

Methods:

- <code title="get /healthz">client.healthz.<a href="./src/simplechecks/resources/healthz.py">check</a>() -> <a href="./src/simplechecks/types/healthz_check_response.py">HealthzCheckResponse</a></code>

# Account

Types:

```python
from simplechecks.types import AccountRetrieveResponse
```

Methods:

- <code title="get /v1/account">client.account.<a href="./src/simplechecks/resources/account.py">retrieve</a>() -> <a href="./src/simplechecks/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>

# Checks

Types:

```python
from simplechecks.types import Check, CheckListResponse
```

Methods:

- <code title="post /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks.py">create</a>(\*\*<a href="src/simplechecks/types/check_create_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks.py">retrieve</a>(id) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="patch /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks.py">update</a>(id, \*\*<a href="src/simplechecks/types/check_update_params.py">params</a>) -> <a href="./src/simplechecks/types/check.py">Check</a></code>
- <code title="get /v1/checks">client.checks.<a href="./src/simplechecks/resources/checks.py">list</a>(\*\*<a href="src/simplechecks/types/check_list_params.py">params</a>) -> <a href="./src/simplechecks/types/check_list_response.py">CheckListResponse</a></code>
- <code title="delete /v1/checks/{id}">client.checks.<a href="./src/simplechecks/resources/checks.py">delete</a>(id) -> None</code>
