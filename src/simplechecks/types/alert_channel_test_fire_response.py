# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AlertChannelTestFireResponse"]


class AlertChannelTestFireResponse(BaseModel):
    enqueued: int
    """1 if a new dispatch was enqueued, 0 if it deduped."""

    incident_id: str
    """Synthetic incident id for the test dispatch."""
