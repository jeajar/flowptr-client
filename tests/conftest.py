import os

import pytest

from shotgrid_client.config import ShotgridSettings


@pytest.fixture
def test_settings():
    return ShotgridSettings(
        client_id="test_client",
        client_secret="test_secret",
        domain="https://test.shotgunstudio.com/",
        api_version="api/v1",
    )


@pytest.fixture(scope="session", autouse=True)
def session_env():
    """Setup test environment variables for entire test session"""
    # Store original env vars
    original_env = {}
    for key in os.environ:
        if key.startswith("FPT_"):
            original_env[key] = os.environ[key]
            del os.environ[key]

    # Set test vars
    test_vars = {
        "FPT_CLIENT_ID": "test_client",
        "FPT_CLIENT_SECRET": "test_secret",
        "FPT_DOMAIN": "https://test.shotgunstudio.com/",
        "FPT_API_VERSION": "api/v1",
    }

    for key, value in test_vars.items():
        os.environ[key] = value

    yield test_vars

    # Restore original env vars
    for key in test_vars:
        del os.environ[key]
    for key, value in original_env.items():
        os.environ[key] = value


@pytest.fixture
def mock_env(monkeypatch):
    """Function-scoped fixture for temporary env var changes"""
    return monkeypatch


@pytest.fixture
def unset_required_env(monkeypatch):
    """Unset required environment variables"""
    monkeypatch.delenv("FPT_CLIENT_ID", raising=False)
    monkeypatch.delenv("FPT_CLIENT_SECRET", raising=False)
    return {
        "FPT_DOMAIN": "https://test.shotgunstudio.com/",
        "FPT_TOKEN_ENDPOINT": "/api/v1/auth/access_token",
        "FPT_API_VERSION": "api/v1",
    }


@pytest.fixture
def mock_token_response():
    return {"access_token": "mock_token", "token_type": "Bearer", "expires_in": 3600}
