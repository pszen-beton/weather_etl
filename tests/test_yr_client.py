import os
from unittest.mock import patch
from clients.Yr_client import YrClient

@patch("clients.base_client.BaseWeatherClient._get")
def test_yr_client_success(mock_get):
    mock_get.return_value = {
        "type": 'Feature',
        "geometry": {'im just': 'a mock :('}
    }
    client = YrClient()
    result = client.fetch_weather_data(52.23, 21.01)
    assert result["type"] == "Feature"
    assert "geometry" in result
    mock_get.assert_called_once_with("https://api.met.no/weatherapi/locationforecast/2.0/complete",
                                     params = {
                                         "lat": 52.23,
                                         "lon": 21.01
                                        },
                                     headers = {"User-Agent": os.getenv("YR_USERAGENT")}
                                     )
