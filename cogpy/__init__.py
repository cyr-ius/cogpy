"""COG Python client for querying the INSEE geographical reference data (COG)."""

from .api import COG
from .exceptions import (
    COGException,
    HttpRequestError,
    RequestException,
    TimeoutExceededError,
)

__all__ = [
    "COG",
    "COGException",
    "HttpRequestError",
    "TimeoutExceededError",
    "RequestException",
]
