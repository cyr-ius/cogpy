"""Custom exceptions for the COG client."""


class COGException(Exception):
    """Base exception for COG errors."""


class HttpRequestError(COGException):
    """Exception raised when a network or communication error occurs."""


class TimeoutExceededError(HttpRequestError):
    """Exception raised when a request times out."""


class RequestException(HttpRequestError):
    """Exception raised when the API returns an HTTP error response."""

    def __init__(
        self, message: str, status: int | None = None, url: str | None = None
    ) -> None:
        self.status = status
        self.url = url
        super().__init__(message)

    def __str__(self) -> str:
        parts = [self.args[0]]
        if self.status:
            parts.insert(0, f"HTTP {self.status}")
        if self.url:
            parts.append(f"({self.url})")
        return " — ".join(parts[:2]) + (f" {parts[2]}" if len(parts) > 2 else "")
