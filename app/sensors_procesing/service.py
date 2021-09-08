from typing import List

from app.sensors.sensor_factory import SensorFactory
from app.sensors_procesing import ProcessedSensorData, CalculatedData
from app.sensors_procesing.calculated_config_repository import CalculatedConfigRepository
from app.sensors_procesing.sensor_config_repository import SensorsConfigRepository
from app.sensors_procesing.sensor_raw_data_repository import SensorsRawDataRepository


class SensorsProcessingService:
    """Get data form repository and process them"""

    def __init__(
            self,
            sensor_config_repository: SensorsConfigRepository,
            sensor_raw_data_repository: SensorsRawDataRepository,
            calculated_config_repo: CalculatedConfigRepository
    ) -> None:
        """
        :param sensor_config_repository: Inject the data from the sensor config repository
        :param sensor_raw_data_repository: Inject the data from the sensor repository
        :param calculated_config_repo: Inject the data from the calculated data repository
        """

        self._sensor_raw_data_repository: SensorsRawDataRepository = sensor_raw_data_repository
        self._sensor_config_repository: SensorsConfigRepository = sensor_config_repository
        self._calculated_config_repository: CalculatedConfigRepository = calculated_config_repo

    def process_sensor_data(self) -> List[ProcessedSensorData]:
        """Process data from sensor"""

        sensors_raw_data = self._sensor_raw_data_repository.get_sensor_raw_data(
            self._sensor_config_repository.get_sensor_config()
        )
        factory = SensorFactory()
        processed_sensors_data = []
        for sensor_raw_data in sensors_raw_data:
            sensor = factory.create_instance(sensor_raw_data)
            if sensor is None:
                # Raise exception
                pass
            processed_sensors_data.append(sensor.get_processed_data())
        return processed_sensors_data

    def get_calculated_data(self) -> List[CalculatedData]:
        """Calculate value with sensor data"""
        pass
