from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import ConfigSensor


class SensorsConfigRepository(ABC):
    """Get the sensor´s config data."""

    @abstractmethod
    def get_sensor_config(self) -> List[ConfigSensor]:
        """Get configuration data of sensors."""
