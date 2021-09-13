from typing import List, Dict

from app.calculated_values.calculate_value_factory import CalculateValueFactory
from app.sensors.sensor_factory import SensorFactory
from app.sensors_procesing import ToCalculateRawData, SettingsCalculate, SensorSpecs
from app.sensors_procesing.calculated_settings_repository import CalculatedSettingsRepository
from app.sensors_procesing.sensor_settings_repository import SensorsSettingsRepository
from app.sensors_procesing.sensor_raw_data_repository import SensorsRawDataRepository


class SensorsProcessingService:
    """Get data form repository and process them"""

    def __init__(
            self,
            sensor_specs_repository: SensorSpecs,
            sensor_config_repository: SensorsSettingsRepository,
            sensor_raw_data_repository: SensorsRawDataRepository,
            calculated_config_repo: CalculatedSettingsRepository,
            sensor_factory: SensorFactory,
            calculate_value_factory: CalculateValueFactory
    ) -> None:

        self._sensor_specs_repository: SensorSpecs = sensor_specs_repository
        self._sensor_raw_data_repository: SensorsRawDataRepository = sensor_raw_data_repository
        self._sensor_config_repository: SensorsSettingsRepository = sensor_config_repository
        self._calculated_settings_repository: CalculatedSettingsRepository = calculated_config_repo
        self._sensor_factory: SensorFactory = sensor_factory
        self._calculate_value_factory: CalculateValueFactory = calculate_value_factory

    def process_sensor_data(self) -> Dict[int, Dict]:
        """Process data from sensor"""

        sensors_raw_data = self._sensor_raw_data_repository.get_sensor_raw_data(
            self._sensor_config_repository.get_sensor_settings()
        )
        processed_sensors_data = {}
        for sensor_raw_data in sensors_raw_data:
            sensor = self._sensor_factory.create_instance(
                sensor_raw_data, self._sensor_specs_repository
            )
            processed_sensors_data.update(sensor.get_processed_data())
        return processed_sensors_data

    def get_calculated_data(
            self, processed_sensors_data: Dict[int, Dict]
    ) -> Dict[int, Dict]:
        """Calculate value with sensor data"""

        to_calculate_settings = self._calculated_settings_repository.get_calculated_settings()
        raw_values_to_calculate = self._get_raw_data_to_calculate(
            to_calculate_settings, processed_sensors_data
        )
        calculated_data = {}
        for raw_data in raw_values_to_calculate:
            calculated = self._calculate_value_factory.create_calculate_value_instance(raw_data)
            calculated_data.update(calculated.get_calculated_value())
        return calculated_data

    def _get_raw_data_to_calculate(
            self,
            values_to_calculate: List[SettingsCalculate],
            processed_sensors_data: Dict[int, Dict]
    ) -> List[ToCalculateRawData]:
        """Get the value from sensors."""

        return [
            ToCalculateRawData(
                settings=to_calculate,
                sensor_1_value=processed_sensors_data[to_calculate.sensor_1_id]["value"],
                sensor_2_value=processed_sensors_data[to_calculate.sensor_2_id]["value"],
            ) for to_calculate in values_to_calculate
        ]
