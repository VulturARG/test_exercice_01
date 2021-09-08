from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import CalculatedData


class CalculatedConfigRepository(ABC):
    """Get the sensor´s config data."""

    name = ""

    @abstractmethod
    def get_calculated_config(self) -> List[CalculatedData]:
        """Get configuration data of sensors."""
