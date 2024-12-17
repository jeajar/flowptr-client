from unittest.mock import Mock, patch

import pytest
from httpx import Response

from shotgrid_client.client import ShotgridClient
from shotgrid_client.config import ShotgridSettings


@pytest.fixture
def mock_client():
    with patch("shotgrid_client.client.AsyncOAuth2Client") as mock:
        oauth_client = Mock()
        mock.return_value = oauth_client

        # Setup mock responses
        response = Mock(spec=Response)
        response.json.return_value = {"data": "test"}
        response.raise_for_status = Mock()
        oauth_client.request.return_value = response

        # Setup token fetch
        oauth_client.fetch_token.return_value = {"access_token": "test_token"}

        yield oauth_client


@pytest.fixture
def client(mock_client):
    return ShotgridClient()


@pytest.mark.asyncio
async def test_init_default_config():
    client = ShotgridClient()
    assert isinstance(client.config, ShotgridSettings)
    assert client.token is None


@pytest.mark.asyncio
async def test_init_custom_config():
    config = ShotgridSettings(base_url="https://custom.shotgrid.com")
    client = ShotgridClient(config)
    assert client.config.base_url == "https://custom.shotgrid.com"


@pytest.mark.asyncio
async def test_ensure_token(client, mock_client):
    await client._ensure_token()
    mock_client.fetch_token.assert_called_once()
    assert client.token == {"access_token": "test_token"}


@pytest.mark.asyncio
async def test_update_token(client):
    new_token = {"access_token": "new_token"}
    client._update_token(new_token)
    assert client.token == new_token


@pytest.mark.asyncio
async def test_get(client, mock_client):
    result = await client.get("/endpoint", {"param": "value"})
    mock_client.request.assert_called_with(
        "GET",
        f"{client.config.base_url}/endpoint",
        params={"param": "value"},
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert result == {"data": "test"}


@pytest.mark.asyncio
async def test_post(client, mock_client):
    data = {"test": "data"}
    result = await client.post("/endpoint", data)
    mock_client.request.assert_called_with(
        "POST",
        f"{client.config.base_url}/endpoint",
        json=data,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert result == {"data": "test"}


@pytest.mark.asyncio
async def test_put(client, mock_client):
    data = {"test": "data"}
    result = await client.put("/endpoint", data)
    mock_client.request.assert_called_with(
        "PUT",
        f"{client.config.base_url}/endpoint",
        json=data,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )
    assert result == {"data": "test"}


@pytest.mark.asyncio
async def test_delete(client, mock_client):
    await client.delete("/endpoint")
    mock_client.request.assert_called_with(
        "DELETE",
        f"{client.config.base_url}/endpoint",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
    )


@pytest.mark.asyncio
async def test_request_error(client, mock_client):
    mock_client.request.return_value.raise_for_status.side_effect = Exception(
        "API Error"
    )

    with pytest.raises(Exception, match="API Error"):
        await client.get("/endpoint")


@pytest.mark.asyncio
async def test_ensure_token_cached(client, mock_client):
    client.token = {"access_token": "existing_token"}
    await client._ensure_token()
    mock_client.fetch_token.assert_not_called()
