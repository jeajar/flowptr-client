import httpx
import pytest
import respx

from flowptr_client.client import FlowPTRClient


@pytest.fixture
def client(test_settings):
    """Create a test client instance"""
    # Remove async since ShotgridClient.__init__ is not async
    return FlowPTRClient(config=test_settings)


@pytest.mark.asyncio
async def test_token_fetch(client, mock_token_response):
    """Test initial token fetch"""
    with respx.mock(assert_all_mocked=False) as mock:
        # Match exact URL and headers
        mock.post(
            "https://test.shotgunstudio.com/api/v1/auth/access_token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            },
        ).respond(json=mock_token_response)

        await client._ensure_token()
        assert client.token is not None
        assert client.token["access_token"] == mock_token_response["access_token"]


@pytest.mark.asyncio
async def test_token_refresh(client, mock_token_response):
    """Test token refresh when expired"""
    with respx.mock() as mock:
        # Initial token
        mock.post(str(client.config.auth_endpoint)).respond(
            json=mock_token_response, status_code=200
        )

        # Simulate token expiry
        client.token = None

        # Should fetch new token
        await client._ensure_token()
        assert client.token is not None
        assert mock.calls.call_count == 1


@pytest.mark.asyncio
async def test_get_request(client, mock_token_response):
    """Test GET request"""
    test_data = {"key": "value"}

    with respx.mock() as mock:
        # Mock token endpoint
        mock.post(str(client.config.auth_endpoint)).respond(
            json=mock_token_response, status_code=200
        )

        # Mock GET endpoint
        mock.get(f"{client.config.base_url}test").respond(
            json=test_data, status_code=200
        )

        response = await client.get("test")
        assert response == test_data
        assert mock.calls.call_count == 2  # Token fetch + GET request


@pytest.mark.asyncio
async def test_post_request(client, mock_token_response):
    """Test POST request"""
    request_data = {"post": "data"}
    response_data = {"status": "success"}

    with respx.mock() as mock:
        mock.post(str(client.config.auth_endpoint)).respond(
            json=mock_token_response, status_code=200
        )

        mock.post(f"{client.config.base_url}test").respond(
            json=response_data, status_code=200
        )

        response = await client.post("test", json=request_data)
        assert response == response_data
        assert mock.calls.last.request.content == b'{"post": "data"}'


@pytest.mark.asyncio
async def test_request_headers(client, mock_token_response):
    """Test request headers are set correctly"""
    with respx.mock() as mock:
        mock.post(str(client.config.auth_endpoint)).respond(
            json=mock_token_response, status_code=200
        )

        mock.get(f"{client.config.base_url}test").respond(json={}, status_code=200)

        await client.get("test")
        assert mock.calls.last.request.headers["Accept"] == "application/json"
        assert mock.calls.last.request.headers["Content-Type"] == "application/json"


@pytest.mark.asyncio
async def test_error_handling(client, mock_token_response):
    """Test error handling for failed requests"""
    with respx.mock() as mock:
        mock.post(str(client.config.auth_endpoint)).respond(
            json=mock_token_response, status_code=200
        )

        mock.get(f"{client.config.base_url}test").respond(status_code=404)

        with pytest.raises(httpx.HTTPError):
            await client.get("test")
