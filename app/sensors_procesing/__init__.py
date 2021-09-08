from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigSensor:
    id: int
    type: str


@dataclass(frozen=True)
class RawSensorData:
    first_raw_value: int
    second_raw_value: int


@dataclass(frozen=True)
class ProcessedSensorData:
    type: str
    value: float
    unit: str
    status: str


@dataclass(frozen=True)
class CalculatedData:
    type: str
    sensor_1_id: int
    sensor_2_id: int
    value: float
    unit: str
    status: str


