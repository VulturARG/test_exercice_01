import unittest
from unittest.mock import Mock

from app.sensors_procesing import ConfigSensor, RawSensorData, ProcessedSensorData
from app.sensors_procesing.calculated_config_repository import CalculatedConfigRepository
from app.sensors_procesing.sensor_config_repository import SensorsConfigRepository
from app.sensors_procesing.sensor_raw_data_repository import SensorsRawDataRepository
from app.sensors_procesing.service import SensorsProcessingService


class TestSensorsProcessing(unittest.TestCase):
    def setUp(self):
        self._config_sensor_0 = ConfigSensor(
            id=0,
            type="DBT"
        )
        self._raw_data_none = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=None,
            second_raw_value=None,
        )

        self._raw_data_positive_temp = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=1,
            second_raw_value=4,
        )

    def test_sensor_input(self):
        expected = [
            ProcessedSensorData(
                id=0,
                type="DBT",
                value=26,
                unit="ºC",
                status="OK"
            )
        ]
        test_cases = [
            ([self._config_sensor_0], [self._raw_data_positive_temp], [], expected, "DBT Sensor 26ºC"),

        ]

        sensor_config_repository = Mock(spec=SensorsConfigRepository)
        sensor_raw_data_repository = Mock(spec=SensorsRawDataRepository)
        calculated_data_repository = Mock(spec=CalculatedConfigRepository)

        service = SensorsProcessingService(
            sensor_config_repository=sensor_config_repository,
            sensor_raw_data_repository=sensor_raw_data_repository,
            calculated_config_repo=calculated_data_repository
        )

        for sensor_config, sensor_raw_data, calculated_data, expected, message in test_cases:
            # values returned by the repositories
            sensor_config_repository.get_sensor_config.return_value = sensor_config
            sensor_raw_data_repository.get_sensor_raw_data.return_value = sensor_raw_data
            calculated_data_repository.get_calculated_config.return_value = calculated_data

            actual = service.process_sensor_data()

            with self.subTest(message):
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
