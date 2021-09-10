from typing import List

from app.calculated_values import CalculateValue
from app.sensors_procesing import (
    CalculatedData,
    ToCalculateRawData
)


class Dew(CalculateValue):
    """Calculate values from sensor data."""

    def __init__(self, to_calculate_raw_data: ToCalculateRawData) -> None:
        super().__init__(to_calculate_raw_data)
        self._to_calculate_raw_data = to_calculate_raw_data

    def get_calculated_value(self) -> CalculatedData:
        """Calculate value with data of sensors."""



