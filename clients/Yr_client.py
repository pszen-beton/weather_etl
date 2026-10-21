import os
from clients.base_client import BaseWeatherClient

class YrClient(BaseWeatherClient):

    BASE_URL = "https://api.met.no/weatherapi/locationforecast/2.0/complete"
    def fetch_weather_data(self, lat: float, lon: float) -> dict:
        params = {
            "lat": lat,
            "lon": lon
        }

        user_agent = os.getenv("YR_USERAGENT")
        headers = {"User-Agent": user_agent}

        data = self._get(self.BASE_URL, params=params, headers=headers)

        return data