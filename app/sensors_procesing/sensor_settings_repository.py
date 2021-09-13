from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import SettingsSensor


class SensorsSettingsRepository(ABC):
    """Get the sensor´s settings data."""

    @abstractmethod
    def get_sensor_settings(self) -> List[SettingsSensor]:
        """Get settings data of sensors."""
