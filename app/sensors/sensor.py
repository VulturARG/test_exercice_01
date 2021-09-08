from abc import ABC, abstractmethod

from app.sensors_procesing import ProcessedSensorData


class Sensors(ABC):
    """Generic sensor"""

    name = ""

    @abstractmethod
    def get_value(self) -> ProcessedSensorData:
        pass

    @abstractmethod
    def _check_data_integrity(self) -> bool:
        pass

    @abstractmethod
    def _check_error_from_sensor(self) -> bool:
        pass
