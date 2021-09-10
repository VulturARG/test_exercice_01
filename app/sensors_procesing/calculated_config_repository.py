from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import ConfigCalculate


class CalculatedConfigRepository(ABC):
    """Get the sensor´s config data."""

    @abstractmethod
    def get_calculated_config(self) -> List[ConfigCalculate]:
        """Get configuration data of sensors."""
