import pytest

from shotgrid_client.config import ShotgridSettings


def test_config_loads_from_env(session_env):
    """Test config loads from environment variables"""
    settings = ShotgridSettings()
    assert settings.client_id == session_env["FPT_CLIENT_ID"]
    assert settings.client_secret == session_env["FPT_CLIENT_SECRET"]
    assert str(settings.domain) == session_env["FPT_DOMAIN"]
    assert settings.api_version == session_env["FPT_API_VERSION"]


def test_global_config_instance(session_env):
    """Test global config instance has test values"""
    config = ShotgridSettings()
    assert config.client_id == session_env["FPT_CLIENT_ID"]
    assert config.client_secret == session_env["FPT_CLIENT_SECRET"]


def test_invalid_domain():
    """Test domain URL validation"""
    with pytest.raises(ValueError):
        ShotgridSettings(client_id="test", client_secret="test", domain="invalid-url")


def test_missing_required_fields(monkeypatch):
    """Test missing required fields raises error"""
    monkeypatch.delenv("FPT_CLIENT_ID")
    monkeypatch.delenv("FPT_CLIENT_SECRET")

    with pytest.raises(ValueError):
        ShotgridSettings()
