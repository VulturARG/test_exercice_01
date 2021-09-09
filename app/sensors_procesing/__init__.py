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
        "W_V": {"min": 0, "max": 250, "unit": "kmh"},
        "W_D": {"min": 0, "max": 359, "unit": "º"}
    }
