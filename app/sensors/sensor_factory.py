from inspect import getmembers, isclass, isabstract
import app.sensors as sensors

from app.sensors_procesing import RawSensorData


class SensorFactory:
    sensors = {}  # key = sensor type, Value = class for the sensor

    def __init__(self):
        self.load_sensors()

    def load_sensors(self) -> None:
        classes = getmembers(
            sensors,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, sensors.Sensor):
                self.sensors.update([[name, _type]])

    def create_instance(self, raw_data: RawSensorData) -> sensors:
        name = raw_data.type
        return self.sensors[name](raw_data) if name in self.sensors else None
