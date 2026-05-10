# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AlertTestFireResponse"]


class AlertTestFireResponse(BaseModel):
    channel_count: int
    """Total channels configured on the check."""

    enqueued: int
    """Number of dispatches accepted (un-deduped)."""

    incident_id: str
    """
    Synthetic incident id used to dedupe the test dispatches against accidental
    double-clicks.
    """
