from abc import ABC, abstractmethod

from app.sensors_procesing import (
    CalculatedData,
    ToCalculateRawData
)


class CalculateValue(ABC):
    """Calculate values from sensor data."""

    def __init__(self, to_calculate_raw_data: ToCalculateRawData) -> None:
        self._to_calculate_raw_data = to_calculate_raw_data

    @abstractmethod
    def get_calculated_value(self) -> CalculatedData:
        """Calculate value with data of sensors."""


