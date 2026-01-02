"""Common types and enums used across the FlowPTR client."""

from enum import Enum


class RequestType(str, Enum):
    """Types of operations supported in batch requests."""

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


class GrantType(str, Enum):
    """OAuth 2.0 grant types supported by Flow Production Tracking.

    Attributes:
        CLIENT_CREDENTIALS: API script authentication using client_id/client_secret
        PASSWORD: User authentication with username/password (supports 2FA)
        SESSION_TOKEN: Custom grant type using existing session tokens
        REFRESH_TOKEN: Exchange refresh token for new access token
    """

    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"
    SESSION_TOKEN = "session_token"
    REFRESH_TOKEN = "refresh_token"


class ReturnOnly(str, Enum):
    """Filter options for which records to return.

    Attributes:
        ACTIVE: Return only active (non-retired) records
        RETIRED: Return only retired records
    """

    ACTIVE = "active"
    RETIRED = "retired"
