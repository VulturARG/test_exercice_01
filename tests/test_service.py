import unittest
from unittest.mock import Mock

from app.sensors_procesing.calculated_config_repository import CalculatedConfigRepository
from app.sensors_procesing.sensor_config_repository import SensorsConfigRepository
from app.sensors_procesing.sensor_repository import SensorsRepository
from app.sensors_procesing.service import SensorsProcessingService


class TestSensorsProcessing(unittest.TestCase):
    def setUp(self):
        pass

    def test_sensor_input(self):
        test_cases = [
            ({}, {}, {}, False, "Sensor has not data"),

        ]

        sensor_config_repository = Mock(spec=CalculatedConfigRepository)
        sensor_repository = Mock(spec=SensorsRepository)
        calculated_data_repository = Mock(spec=SensorsConfigRepository)

        service = SensorsProcessingService(
            sensor_config_repository=sensor_config_repository,
            sensor_repository=sensor_repository,
            calculated_data_repository=calculated_data_repository
        )

        for sensor_config, sensor_data, calculated_data, expected, message in test_cases:
            # values returned by the repositories
            sensor_config_repository.get_debts.return_value = sensor_config
            sensor_repository.get_payment_plan.return_value = sensor_data
            calculated_data_repository.get_payment.return_value = calculated_data

            actual = service.process_sensor_data()

            with self.subTest(message):
                self.assertEqual(expected, actual[0].is_in_payment_plan)


if __name__ == '__main__':
    unittest.main()
