from typing import Optional, Dict

from app.sensors import Sensor
from app.sensors_procesing import RawSensorData, SensorSpecs, \
    SensorRawDataError, SensorValueOutOfRange


class SensorTypeOne(Sensor):
    """Family sensor type one."""

    def __init__(self, raw_data: RawSensorData, sensor_specs: SensorSpecs) -> None:
        super().__init__(raw_data, sensor_specs)

    def get_processed_data(self) -> Dict:
        """Get the data processed from raw data."""

        status, type_sensor, value = self._get_parameters()

        return {
            self._raw_data.id: {
                "type": type_sensor,
                "value": value,
                "unit": self._sensor_specs.specs[type_sensor].unit,
                "status": status
            }
        }

    def _get_parameters(self):
        type_sensor = self._raw_data.type
        status = None
        value = None
        try:
            self._does_the_data_have_integrity()
            self._is_error_from_sensor()
            value = self._get_value()
            self._is_value_out_of_range(type_sensor, value)
            status = "OK"
        except (SensorRawDataError, TypeError):
            status = "SE"
        except SensorValueOutOfRange:
            status = "OoR"
            value = None

        return status, type_sensor, value

    def _get_value(self) -> Optional[float]:
        """Get sensor value from raw data."""

        raise NotImplementedError

    def _does_the_data_have_integrity(self) -> None:
        """Check if both values are minor than 255."""

        in_range = self._raw_data.first_raw_value < 256 and self._raw_data.second_raw_value < 256
        if not in_range:
            raise SensorRawDataError

    def _is_error_from_sensor(self) -> None:
        """Check if both values are equal to 255."""

        is_error = self._raw_data.first_raw_value == 255 and self._raw_data.second_raw_value == 255
        if is_error:
            raise SensorRawDataError

    def _is_value_out_of_range(self, type_sensor: str, value: float) -> None:
        """Check if the value is within the manufacturer's specifications."""

        minimum = self._sensor_specs.specs[type_sensor].min
        maximum = self._sensor_specs.specs[type_sensor].max
        sensor_in_range = minimum <= value <= maximum
        if not sensor_in_range:
            raise SensorValueOutOfRange

    def _do_math(self):
        """Convert to 8 bits numbers to real"""

        return self._raw_data.first_raw_value * 256 + self._raw_data.second_raw_value
