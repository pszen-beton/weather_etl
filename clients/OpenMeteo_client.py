from clients.base_client import BaseWeatherClient

class OpenMeteoClient(BaseWeatherClient):

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def fetch_weather_data(self, lat: float, lon: float) -> dict:
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
            "past_days": 1,
            "forecast_days": 1,
        }

        data = self._get(self.BASE_URL, params=params)

        return data