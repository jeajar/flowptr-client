"""Custom exceptions for FlowPTR client.

This module defines the exception hierarchy for handling errors from the
Flow Production Tracking REST API and network-level errors.
"""

from typing import Any, Optional


class FlowPTRError(Exception):
    """Base exception for all FlowPTR client errors.

    Attributes:
        message: Error message describing what went wrong
        status_code: HTTP status code if applicable
        error_code: Shotgrid-specific error code if available
    """

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        error_code: Optional[int] = None,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(message)

    def __str__(self) -> str:
        """Format error message with status and error codes."""
        parts = [self.message]
        if self.status_code:
            parts.append(f"(HTTP {self.status_code})")
        if self.error_code:
            parts.append(f"[Error {self.error_code}]")
        return " ".join(parts)


class FlowPTRHTTPError(FlowPTRError):
    """Base exception for HTTP-related errors from the API.

    Raised when the API returns an HTTP error response (4xx or 5xx).
    """

    pass


class FlowPTRAuthenticationError(FlowPTRHTTPError):
    """Authentication failed or token expired (HTTP 401).

    This typically means:
    - Invalid client_id or client_secret
    - Expired access token that needs refresh
    - Missing authentication credentials
    """

    pass


class FlowPTRAuthorizationError(FlowPTRHTTPError):
    """Insufficient permissions to perform the requested operation (HTTP 403).

    The authenticated user/script doesn't have permission to:
    - Access the requested resource
    - Perform the requested action
    - View/modify specific fields
    """

    pass


class FlowPTRNotFoundError(FlowPTRHTTPError):
    """Requested resource was not found (HTTP 404).

    This can mean:
    - Entity record doesn't exist
    - Invalid entity type name
    - Invalid field name
    - Endpoint doesn't exist
    """

    pass


class FlowPTRValidationError(FlowPTRHTTPError):
    """Request validation failed (HTTP 400).

    Common causes:
    - Invalid field values
    - Missing required fields
    - Malformed filter syntax
    - Invalid entity type
    - Type mismatch in field values
    """

    pass


class FlowPTRServerError(FlowPTRHTTPError):
    """Server-side error occurred (HTTP 500+).

    These errors indicate a problem on the Shotgrid server side:
    - Internal server error
    - Database connection issues
    - Service temporarily unavailable
    - Gateway timeout
    """

    pass


class FlowPTRConnectionError(FlowPTRError):
    """Network connection error occurred.

    Raised when unable to connect to the Shotgrid server:
    - Network unreachable
    - DNS resolution failed
    - Connection refused
    - SSL/TLS errors
    """

    pass


class FlowPTRTimeoutError(FlowPTRError):
    """Request timed out waiting for response.

    The request took longer than the configured timeout period.
    """

    pass


# Mapping from HTTP status codes to exception classes
STATUS_CODE_EXCEPTIONS: dict[int, type[FlowPTRHTTPError]] = {
    400: FlowPTRValidationError,
    401: FlowPTRAuthenticationError,
    403: FlowPTRAuthorizationError,
    404: FlowPTRNotFoundError,
    500: FlowPTRServerError,
    502: FlowPTRServerError,
    503: FlowPTRServerError,
    504: FlowPTRServerError,
}
