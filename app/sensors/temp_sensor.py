from typing import Optional

from app.sensors.sensor_type_one import SensorTypeOne
from app.sensors_procesing import RawSensorData, SensorSpecs


class DBT(SensorTypeOne):
    """Dry Bulb Temperature sensor."""

    def __init__(self, raw_data: RawSensorData, sensor_specs: SensorSpecs) -> None:
        super().__init__(raw_data, sensor_specs)

    def _get_value(self) -> Optional[float]:
        """Get sensor value from raw data."""

        value = self._do_math()
        value = -(value - 1000) if value > 1000 else value
        return value / 10
