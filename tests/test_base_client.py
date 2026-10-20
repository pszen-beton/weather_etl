import pytest
from unittest.mock import patch
import requests
from clients.base_client import BaseWeatherClient

class DummyClient(BaseWeatherClient):
    def fetch_weather_data(self, lat: float, lon: float) -> dict:
        return self._get("https://i-m-a-test-url.com/api")

@patch("requests.Session.get")
def test_base_client_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}

    client = DummyClient()

    result = client.fetch_weather_data(51.5074, 7.4629)
    assert result == {"key": "value"}
    mock_get.assert_called_once()

@patch("requests.Session.get")
def test_base_client_http_error(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 not found")

    client = DummyClient()
    with pytest.raises(requests.exceptions.HTTPError):
        client.fetch_weather_data(51.5074, 7.4629)

@patch("requests.Session.get")
def test_base_client_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("Request timed out")
    client = DummyClient()
    with pytest.raises(requests.exceptions.Timeout):
        client.fetch_weather_data(51.5074, 7.4629)

@patch("requests.Session.get")
def test_base_client_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Network error")

    client = DummyClient()
    with pytest.raises(requests.exceptions.RequestException):
        client.fetch_weather_data(51.5074, 7.4629)