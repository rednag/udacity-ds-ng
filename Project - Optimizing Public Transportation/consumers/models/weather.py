"""Contains functionality related to Weather"""
import logging
import json

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        weather_json = message.value()
        try:
            self.temperature = weather_json["temperature"]
            self.status = weather_json["status"]
        except Exception as e:
            logger.error(f"error processing weather message: {e}")
            pass
