from app.calculated_values import CalculateValue
from app.sensors_procesing import (
    CalculatedData,
    ToCalculateRawData
)


class DEW(CalculateValue):
    """Calculate values from sensor data."""

    def __init__(self, to_calculate_raw_data: ToCalculateRawData) -> None:
        super().__init__(to_calculate_raw_data)

    def get_calculated_value(self) -> CalculatedData:
        """Calculate value with data of sensors."""

        temperature = self._data.sensor_1_value
        humidity = self._data.sensor_2_value
        try:
            dew_point = round((humidity / 100)**(1 / 8) * (110 + temperature) - 110, 1)
            status = "OK"
        except TypeError:
            dew_point = None
            status = "ERROR"

        return CalculatedData(
            settings=self._data.settings,
            value=dew_point,
            status=status
        )




