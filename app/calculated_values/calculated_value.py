from abc import ABC, abstractmethod
from typing import Dict

from app.sensors_procesing import (
    ToCalculateRawData
)


class CalculateValue(ABC):
    """Calculate values from sensor data."""

    def __init__(self, to_calculate_raw_data: ToCalculateRawData) -> None:
        self._data = to_calculate_raw_data

    @abstractmethod
    def get_calculated_value(self) -> Dict[int, Dict]:
        """Calculate value with data of sensors."""

    def _get_formatted_result(self, value, status):
        return {
            self._data.settings.id: {
                "type:": self._data.settings.type,
                "sensor_1_id": self._data.settings.sensor_1_id,
                "sensor_2_id": self._data.settings.sensor_2_id,
                "value": value,
                "unit": self._data.settings.unit,
                "status": status
            }
        }
