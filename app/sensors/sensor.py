from abc import ABC, abstractmethod
from typing import Optional

from app.sensors_procesing import ProcessedSensorData, RawSensorData, SensorSpecs


class Sensor(ABC):
    """Generic sensor"""

    def __init__(self, raw_data: RawSensorData) -> None:
        self._raw_data = raw_data

    @abstractmethod
    def _get_value(self) -> Optional[float]:
        """Get sensor value from raw data."""

    @abstractmethod
    def get_processed_data(self) -> ProcessedSensorData:
        """Get the data processed from raw data."""

    @abstractmethod
    def _check_data_integrity(self) -> bool:
        """Check if both values are minor than 255."""

    @abstractmethod
    def _check_error_from_sensor(self) -> bool:
        """Check if both values are equal to 255."""

    @abstractmethod
    def _check_out_of_range(self, type_sensor: str, value: float) -> bool:
        """Check if the value is within the manufacturer's specifications."""

