from typing import List

from app.sensors_procesing import ProcessedSensorData, CalculatedData
from app.sensors_procesing.calculated_config_repository import CalculatedConfigRepository
from app.sensors_procesing.sensor_config_repository import SensorsConfigRepository
from app.sensors_procesing.sensor_repository import SensorsRepository


class SensorsProcessingService:
    """Get data form repository and process them"""

    def __init__(
            self,
            sensor_config_repository: SensorsConfigRepository,
            sensor_repository: SensorsRepository,
            calculated_data_repository: CalculatedConfigRepository
    ) -> None:
        """
        :param sensor_config_repository: Inject the data from the sensor config repository
        :param sensor_repository: Inject the data from the sensor repository
        :param calculated_data_repository: Inject the data from the calculated data repository
        """

        self._sensor_repository: SensorsRepository = sensor_repository
        self._sensor_config_repository: SensorsConfigRepository = sensor_config_repository
        self._calculated_data_repository: CalculatedConfigRepository = calculated_data_repository

    def process_sensor_data(self) -> List[ProcessedSensorData]:
        """Process data from sensor"""
        pass

    def get_calculated_data(self) -> List[CalculatedData]:
        """Calculate value with sensor data"""
        pass
