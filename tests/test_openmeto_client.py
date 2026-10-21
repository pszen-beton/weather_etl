from unittest.mock import patch
from clients.OpenMeteo_client import OpenMeteoClient

@patch("clients.base_client.BaseWeatherClient._get")
def test_openmeteo_client_success(mock_get):
    mock_get.return_value = {
        "latitude": 52.23,
        "longitude": 21.01,
        "hourly": {"temperature_2m": [0.0, 1.0], "precipation": [0.0, 1.0], "wind_speed_10m": [0.0, 1.0]},
    }
    client = OpenMeteoClient()
    result = client.fetch_weather_data(52.23, 21.01)
    assert result["latitude"] == 52.23
    assert "hourly" in result
    mock_get.assert_called_once_with("https://api.open-meteo.com/v1/forecast",
                                     params = {
                                         "latitude": 52.23,
                                         "longitude": 21.01,
                                         "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
                                         "past_days": 1,
                                         "forecast_days": 1
                                        }
                                     )
