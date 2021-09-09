from abc import ABC, abstractmethod
from typing import Optional

from app.sensors import Sensor
from app.sensors_procesing import ProcessedSensorData, RawSensorData, SensorSpecs


class SensorTypeOne(Sensor):
    """Family sensor type one."""

    def __init__(self, raw_data: RawSensorData):
        self._raw_data = raw_data

    def _get_value(self) -> Optional[float]:
        """Get sensor value from raw data."""

        raise NotImplementedError

    def get_processed_data(self) -> ProcessedSensorData:
        """Get the data processed from raw data."""

        status = "OK"
        value = self._get_value()
        type_sensor = self._raw_data.type

        if not self._check_data_integrity() or self._check_error_from_sensor():
            status = "SE"
            value = None
        elif value is not None and self._check_out_of_range(type_sensor, value):
            status = "OoR"
            value = None

        return ProcessedSensorData(
            id=self._raw_data.id,
            type=type_sensor,
            value=value,
            unit=SensorSpecs.TYPE.value[type_sensor]["unit"],
            status=status
        )

    def _check_data_integrity(self) -> bool:
        """Check if both values are minor than 255."""

        return self._raw_data.first_raw_value <= 255 and self._raw_data.second_raw_value <= 255

    def _check_error_from_sensor(self) -> bool:
        """Check if both values are equal to 255."""

        return self._raw_data.first_raw_value == 255 and self._raw_data.second_raw_value == 255

    def _check_out_of_range(self, type_sensor: str, value: float) -> bool:
        """Check if the value is within the manufacturer's specifications."""

        minimum = SensorSpecs.TYPE.value[type_sensor]["min"]
        maximum = SensorSpecs.TYPE.value[type_sensor]["max"]
        return value < minimum or maximum < value
