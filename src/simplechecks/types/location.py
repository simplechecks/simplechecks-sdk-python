# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    """
    One deployed (provider, data-center) tuple where Simple Checks
    runs garrisons, with geographic metadata + live status.
    """

    id: str
    """Composite identifier; `<provider>:<location>` (e.g. `aws:us-east-1`)."""

    city: str

    continent: Literal["NA", "SA", "EU", "AS", "AF", "OC", "AN"]

    country: str
    """ISO 3166-1 alpha-2 country code."""

    location: str
    """Provider-native data-center id (varies in format per provider)."""

    provider: str
    """Cloud provider."""

    status: Literal["provisioning", "ready", "degraded", "unprovisioned", "draining", "maintenance", "scaling"]
    """Live garrison status as reported by command-center.

    The endpoint returns the garrison's stored status verbatim, so this enum lists
    every value the state machine can surface: `provisioning` — a garrison row
    exists but is not yet serving; `ready` — serving normally; `degraded` — serving
    but a broken-probe signal is firing; `unprovisioned` — the location is
    code-defined but no garrison row exists yet (deploy pending), typically greyed
    out in the dashboard; `draining`, `maintenance`, `scaling` — sticky operator-set
    states that automated transitions preserve rather than clobber.
    """

    lat: Optional[float] = None
    """Metro-center latitude (degrees, WGS84)."""

    lon: Optional[float] = None
    """Metro-center longitude (degrees, WGS84)."""

    metro: Optional[str] = None
    """
    IATA-style 3-letter code for the nearest major metro. Empty for the mock
    provider; "loose anchor" (not a precise claim) for non-airport-adjacent sites
    like Hetzner Falkenstein.
    """
