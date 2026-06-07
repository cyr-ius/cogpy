"""HTTP request handler for the COG API client."""

import asyncio
import logging
import socket
from typing import Any

from aiohttp import ClientError, ClientResponseError, ClientSession

from .exceptions import HttpRequestError, RequestException, TimeoutExceededError

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "HTTPRequest",
    "HttpRequestError",
    "RequestException",
    "TimeoutExceededError",
]


class HTTPRequest:
    """Base class for handling HTTP requests to the API."""

    TIMEOUT = 120

    def __init__(
        self, session: ClientSession | None = None, timeout: int = TIMEOUT
    ) -> None:
        """Initialize."""
        self.timeout = timeout
        self.session = session or ClientSession()

    async def async_request(self, path: str, method: str = "get", **kwargs: Any) -> Any:
        """Send an HTTP request and return the JSON response."""
        contents = {}
        response = None
        try:
            async with asyncio.timeout(self.timeout):
                if self.session is None:
                    raise HttpRequestError("ClientSession is not initialized.")
                _LOGGER.debug("Request: %s (%s) - %s", path, method, kwargs)
                response = await self.session.request(method, path, **kwargs)
                response.raise_for_status()
                contents = await response.json()
        except (asyncio.CancelledError, asyncio.TimeoutError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to API."
            ) from error
        except ClientResponseError as error:
            status = error.status
            url = str(error.request_info.url)
            if response is not None:
                try:
                    if "application/json" in response.headers.get("Content-Type", ""):
                        body = await response.json()
                        message = body.get("detail") or body.get("message") or str(body)
                    else:
                        message = (await response.read()).decode(
                            "utf-8"
                        ).strip() or error.message
                except ClientError:
                    message = error.message
            else:
                message = "No response received."
            raise RequestException(message, status=status, url=url) from error
        except (ClientError, socket.gaierror) as error:
            raise HttpRequestError(
                "Error occurred while communicating with API."
            ) from error

        return contents

    async def async_close(self) -> None:
        """Close the HTTP session."""
        if self.session:
            await self.session.close()
            self.session = None
