from typing import List

from app.calculated_values.calculate_value_factory import CalculateValueFactory
from app.sensors.sensor_factory import SensorFactory
from app.sensors_procesing import ProcessedSensorData, CalculatedData, TypeSensorNotFoundError, \
    ToCalculateRawData, FormulaToCalculateNotFoundError, ConfigCalculate
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
            processed_sensors_data.append(sensor.get_processed_data())
        return processed_sensors_data

    def get_calculated_data(
            self, processed_sensors_data: List[ProcessedSensorData]
    ) -> List[CalculatedData]:
        """Calculate value with sensor data"""

        to_calculate_config = self._calculated_config_repository.get_calculated_config()
        raw_values_to_calculate = self._get_raw_data_to_calculate(
            to_calculate_config, processed_sensors_data
        )
        factory = CalculateValueFactory()
        calculated_data = []
        for raw_data in raw_values_to_calculate:
            calculated = factory.calculate_values(raw_data)
            if calculated is None:
                raise FormulaToCalculateNotFoundError
            calculated_data.append(calculated)
        return calculated_data

    def _get_raw_data_to_calculate(
            self,
            values_to_calculate: List[ConfigCalculate],
            processed_sensors_data: List[ProcessedSensorData]
    ) -> List[ToCalculateRawData]:
        """Get the value from sensors."""

        for to_calculate in values_to_calculate:
            for sensor_data in processed_sensors_data
