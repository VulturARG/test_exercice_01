from typing import Optional

from app.sensors.sensor_type_one import SensorTypeOne
from app.sensors_procesing import RawSensorData, SensorSpecs


class WiV(SensorTypeOne):
    """Pressure sensor"""

    def __init__(self, raw_data: RawSensorData, sensor_specs: SensorSpecs) -> None:
        super().__init__(raw_data, sensor_specs)

    def _get_value(self) -> Optional[float]:
        """Get sensor value from raw data."""

        return self._do_math() / 100
