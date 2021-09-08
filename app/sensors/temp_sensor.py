from typing import Optional

from app.sensors.sensor import Sensor
from app.sensors_procesing import ProcessedSensorData, RawSensorData, SensorSpecs


class DBT(Sensor):
    """Dry Bulb Temperature"""

    def __init__(self, raw_data: RawSensorData):
        self._raw_data = raw_data

    def get_processed_data(self) -> ProcessedSensorData:
        value = self._get_value()
        status = "OK"
        type_sensor = self._raw_data.type
        return ProcessedSensorData(
            id=self._raw_data.id,
            type=type_sensor,
            value=value,
            unit=SensorSpecs.TYPE.value[type_sensor]["unit"],
            status=status
        )

    def _check_data_integrity(self) -> bool:
        pass

    def _check_error_from_sensor(self) -> bool:
        pass

    def _check_out_of_range(self) -> bool:
        pass

    def _get_value(self) -> Optional[float]:
        return (self._raw_data.first_raw_value * 256 + self._raw_data.second_raw_value) / 10
