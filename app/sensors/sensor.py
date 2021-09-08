from abc import ABC, abstractmethod
from typing import Optional

from app.sensors_procesing import ProcessedSensorData, RawSensorData


class Sensor(ABC):
    """Generic sensor"""

    def __init__(self, raw_data: RawSensorData):
        self._raw_data = raw_data

    @abstractmethod
    def get_processed_data(self) -> ProcessedSensorData:
        pass

    @abstractmethod
    def _check_data_integrity(self) -> bool:
        pass

    @abstractmethod
    def _check_error_from_sensor(self) -> bool:
        pass

    @abstractmethod
    def _check_out_of_range(self) -> bool:
        pass

    @abstractmethod
    def _get_value(self) -> Optional[float]:
        pass
