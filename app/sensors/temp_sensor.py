from typing import Optional

from app.sensors.sensor import Sensor
from app.sensors_procesing import RawSensorData


class DBT(Sensor):
    """Dry Bulb Temperature"""

    def __init__(self, raw_data: RawSensorData):
        super().__init__(raw_data)
        self._raw_data = raw_data

    def _get_value(self) -> Optional[float]:
        value = self._raw_data.first_raw_value * 256 + self._raw_data.second_raw_value
        value = -(value - 1000) if value > 1000 else value
        return value / 10
