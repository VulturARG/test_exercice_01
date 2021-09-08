from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import RawSensorData


class SensorsRepository(ABC):
    """Comunicate with sensors to get they data."""

    name = ""

    @abstractmethod
    def get_sensor_data(self) -> List[RawSensorData]:
        """
        Get sensor data from a source.

        :return: list of  RawSensorData
        """
