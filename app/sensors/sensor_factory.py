from inspect import getmembers, isclass, isabstract
from typing import Dict, Type

import app.sensors as sensors_package
from app.sensors import Sensor

from app.sensors_procesing import RawSensorData, TypeSensorNotFoundError, SensorSpecs


class SensorFactory:
    """Get an instance of Sensor's child class."""

    _sensors: Dict[str, Type[Sensor]] = {}  # key = sensor type

    def __init__(self):
        self._load_sensors()

    def _load_sensors(self) -> None:
        """Populate the _sensors dictionary with classes of sensors package"""

        classes = getmembers(
            sensors_package,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, sensors_package.Sensor):
                self._sensors.update([[name, _type]])

    def create_instance(
            self, raw_data: RawSensorData, sensor_specs: SensorSpecs
    ) -> Sensor:
        """Create the solicited instance."""

        try:
            return self._sensors[raw_data.type](raw_data, sensor_specs)
        except KeyError:
            raise TypeSensorNotFoundError

