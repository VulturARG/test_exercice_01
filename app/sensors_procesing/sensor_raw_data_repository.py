from abc import ABC, abstractmethod
from typing import List

from app.sensors_procesing import RawSensorData, ConfigSensor


class SensorsRawDataRepository(ABC):
    """Comunicate with sensors to get they data."""

    name = ""

    @abstractmethod
    def get_sensor_raw_data(self, source: List[ConfigSensor]) -> List[RawSensorData]:
        """
         Get sensor data from a source.

        :param source: Sensor source
        :return:  list of RawSensorData
        """