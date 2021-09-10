import enum
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ConfigSensor:
    id: int
    type: str


@dataclass(frozen=True)
class RawSensorData:
    id: int
    type: str
    first_raw_value: Optional[int]
    second_raw_value: Optional[int]


@dataclass(frozen=True)
class ConfigCalculate:
    id: int
    type: str
    sensor_1: int
    sensor_2: int
    unit: str


@dataclass(frozen=True)
class ToCalculateRawData:
    id: int
    type: str
    sensor_1_value: Optional[float]
    sensor_2_value: Optional[float]


@dataclass(frozen=True)
class ProcessedSensorData:
    id: int
    type: str
    value: Optional[float]
    unit: str
    status: str


@dataclass(frozen=True)
class CalculatedData:
    type: str
    sensor_1_id: int
    sensor_2_id: int
    value: Optional[float]
    unit: str
    status: str


class SensorSource(enum.Enum):
    SOURCE = "https://my-json-server.typicode.com/VulturARG/test_exercice_01"


class SensorSpecs(enum.Enum):
    TYPE = {
        "DBT": {"min": -40, "max": 70, "unit": "ºC"},
        "WBT": {"min": -40, "max": 70, "unit": "ºC"},
        "HUM": {"min": 0, "max": 100, "unit": "%"},
        "PRE": {"min": 300, "max": 1100, "unit": "hPa"},
        "WiV": {"min": 0, "max": 250, "unit": "kmh"},
        "WiD": {"min": 0, "max": 359, "unit": "º"}
    }


class TypeSensorNotFoundError(Exception):
    MESSAGE = "This type sensor does not exist"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class SensorRawDataError(Exception):
    MESSAGE = "There are an error in raw data from sensor"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class SensorValueOutOfRange(Exception):
    MESSAGE = "The value from sensor is out of range"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class FormulaToCalculateNotFoundError(Exception):
    MESSAGE = "This formula was not found"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


