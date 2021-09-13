import enum
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class SettingsSensor:
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
class SettingsCalculate:
    id: int
    type: str
    sensor_1_id: int
    sensor_2_id: int
    unit: str


@dataclass(frozen=True)
class ToCalculateRawData:
    settings: SettingsCalculate
    sensor_1_value: Optional[float]
    sensor_2_value: Optional[float]


@dataclass(frozen=True)
class CalculatedData:
    settings: SettingsCalculate
    value: Optional[float]
    status: str


@dataclass(frozen=True)
class RawSensorSpecs:
    type: str
    min: int
    max: int
    unit: str
    description: str


@dataclass(frozen=True)
class SensorSpecs:
    specs: Dict[str, RawSensorSpecs]


class SensorSource(enum.Enum):
    SOURCE = "https://my-json-server.typicode.com/VulturARG/test_exercice_01"


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


class SensorValueIsNoneError(Exception):
    MESSAGE = "The sensor value is none"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
