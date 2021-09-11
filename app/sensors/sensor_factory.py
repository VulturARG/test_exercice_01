from inspect import getmembers, isclass, isabstract
import app.sensors as sensors_package

from app.sensors_procesing import RawSensorData, TypeSensorNotFoundError


class SensorFactory:
    """Get an instance of the right class."""

    sensors = {}  # key = sensor type, Value = class for the sensor

    def __init__(self):
        self._load_sensors()

    def _load_sensors(self) -> None:
        """Populate the sensors dictionary with classes of sensors package"""

        classes = getmembers(
            sensors_package,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, sensors_package.Sensor):
                self.sensors.update([[name, _type]])

    def create_instance(self, raw_data: RawSensorData) -> sensors:
        """Create the solicited instance."""

        try:
            return self.sensors[raw_data.type](raw_data)
        except KeyError:
            raise TypeSensorNotFoundError

