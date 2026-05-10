# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Incident"]


class Incident(BaseModel):
    """One alert-state lifecycle entry.

    Derived on read from
    `alert_state` + `alert_dispatches` — there's no separate
    incidents table because the data is fully reconstructable
    from the rows the evaluator already writes.
    """

    id: str
    """Incident id (UUID; from `alert_state.current_incident_id`)."""

    check_id: str

    check_name: str

    started_at_unix_ms: int
    """When the evaluator fired the incident (unix-millis)."""

    status: Literal["ongoing", "resolved"]

    resolved_at_unix_ms: Optional[int] = None
    """Unix-millis of the recovery dispatch. Absent on ongoing incidents."""
