from abc import ABC, abstractmethod
import logging
import requests

logger = logging.getLogger(__name__)

class BaseWeatherClient(ABC):

    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()

    def _get(self, url: str, params: dict = None, headers: dict = None) -> dict:

        try:
            logger.info(f"Sending GET request to: {url} with params: {params} and headers: {headers}")
            response = self.session.get(url, params=params, headers=headers, timeout=self.timeout)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            logger.error(f"Request to {url} timed out after {self.timeout} seconds.")
            raise
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred for {url}: {e.response.status_code} - {e.response.text}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred while making the request: {e}")
            raise

    @abstractmethod
    def fetch_weather_data(self, city: str, country: str) -> dict:
        pass
