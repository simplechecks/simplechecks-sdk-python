# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MaintenanceWindow"]


class MaintenanceWindow(BaseModel):
    end_unix_ms: int

    start_unix_ms: int
