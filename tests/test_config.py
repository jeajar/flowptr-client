import pytest

from flowptr_client.config import FlowPTRClientSettings


def test_config_loads_from_env(session_env):
    """Test config loads from environment variables"""
    settings = FlowPTRClientSettings()
    assert settings.CLIENT_ID == session_env["FPT_CLIENT_ID"]
    assert settings.CLIENT_SECRET == session_env["FPT_CLIENT_SECRET"]
    assert str(settings.DOMAIN) == session_env["FPT_DOMAIN"]
    assert settings.API_VERSION == session_env["FPT_API_VERSION"]


def test_global_config_instance(session_env):
    """Test global config instance has test values"""
    config = FlowPTRClientSettings()
    assert config.CLIENT_ID == session_env["FPT_CLIENT_ID"]
    assert config.CLIENT_SECRET == session_env["FPT_CLIENT_SECRET"]


def test_invalid_domain():
    """Test domain URL validation"""
    with pytest.raises(ValueError):
        FlowPTRClientSettings(
            CLIENT_ID="test", CLIENT_SECRET="test", DOMAIN="invalid-url"
        )


def test_missing_required_fields(monkeypatch):
    """Test missing required fields raises error"""
    monkeypatch.delenv("FPT_CLIENT_ID")
    monkeypatch.delenv("FPT_CLIENT_SECRET")

    with pytest.raises(ValueError):
        FlowPTRClientSettings()
