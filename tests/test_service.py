import unittest
from unittest.mock import Mock

from app.sensors_procesing import ConfigSensor, RawSensorData, ProcessedSensorData
from app.sensors_procesing.calculated_config_repository import CalculatedConfigRepository
from app.sensors_procesing.sensor_config_repository import SensorsConfigRepository
from app.sensors_procesing.sensor_raw_data_repository import SensorsRawDataRepository
from app.sensors_procesing.service import SensorsProcessingService


class TestSensorsProcessing(unittest.TestCase):
    def setUp(self):
        self._config_0 = ConfigSensor(id=0, type="DBT")
        self._config_1 = ConfigSensor(id=1, type="HUM")
        self._config_2 = ConfigSensor(id=2, type="PRE")

        self._raw_data_none = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=None,
            second_raw_value=None,
        )
        self._r_d_positive_temp = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=1,
            second_raw_value=4,
        )

        self._r_d_negative_temp = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=4,
            second_raw_value=30,
        )
        self._r_d_out_range = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=456,
            second_raw_value=30,
        )
        self._r_d_error_message = RawSensorData(
            id=0,
            type="DBT",
            first_raw_value=255,
            second_raw_value=255,
        )
        self._r_d_humidity = RawSensorData(
            id=1,
            type="HUM",
            first_raw_value=3,
            second_raw_value=75,
        )
        self._value_out_range = RawSensorData(
            id=100,
            type="HUM",
            first_raw_value=254,
            second_raw_value=254,
        )
        self._r_d_pressure = RawSensorData(
            id=2,
            type="PRE",
            first_raw_value=37,
            second_raw_value=235,
        )

    def test_sensor_input(self):
        expected_pos = [ProcessedSensorData(id=0, type="DBT", value=26, unit="ºC", status="OK")]
        expected_neg = [ProcessedSensorData(id=0, type="DBT", value=-5.4, unit="ºC", status="OK")]
        expected_se = [ProcessedSensorData(id=0, type="DBT", value=None, unit="ºC", status="SE")]
        expected_hum = [ProcessedSensorData(id=1, type="HUM", value=84.3, unit="%", status="OK")]
        expected_hum2 = [ProcessedSensorData(id=100, type="HUM", value=None, unit="%", status="OoR")]
        expected_pre = [ProcessedSensorData(id=2, type="PRE", value=970.7, unit="hPa", status="OK")]
        test_cases = [
            ([self._config_0], [self._r_d_positive_temp], [], expected_pos, "DBT 26ºC"),
            ([self._config_0], [self._r_d_negative_temp], [], expected_neg, "DBT -5.4ºC"),
            ([self._config_0], [self._r_d_out_range], [], expected_se, "Sensor Data Not Integrity"),
            ([self._config_0], [self._r_d_error_message], [], expected_se, "Sensor Error Message"),
            ([self._config_1], [self._r_d_humidity], [], expected_hum, "Sensor Humidity"),
            ([self._config_1], [self._value_out_range], [], expected_hum2, "Sensor Out of Range"),
            ([self._config_2], [self._r_d_pressure], [], expected_pre, "Sensor Pressure"),
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
