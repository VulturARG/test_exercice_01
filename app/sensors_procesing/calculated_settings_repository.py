from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import SettingsCalculate


class CalculatedSettingsRepository(ABC):
    """Get the sensor´s settings data."""

    @abstractmethod
    def get_calculated_settings(self) -> List[SettingsCalculate]:
        """Get settings data of sensors."""
