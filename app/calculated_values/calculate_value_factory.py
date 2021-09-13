from inspect import getmembers, isclass, isabstract
from typing import Optional, Dict, Type

import app.calculated_values as formulas_package
from app.calculated_values import CalculateValue
from app.sensors_procesing import ToCalculateRawData, FormulaToCalculateNotFoundError


class CalculateValueFactory:
    """Get an instance of the CalculateValue's child class."""

    _calculate_values: Dict[str, Type[CalculateValue]] = {}  # key = sensor type

    def __init__(self):
        self._load_calculation_formulas()

    def _load_calculation_formulas(self) -> None:
        """Populate the _calculate_values dictionary with classes of calculate_values package"""

        classes = getmembers(
            formulas_package,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, formulas_package.CalculateValue):
                self._calculate_values.update([[name, _type]])

    def create_calculate_value_instance(
            self, to_calculate_raw_data: ToCalculateRawData
    ) -> CalculateValue:
        """Create CalculateValue instance."""

        name = to_calculate_raw_data.settings.type
        try:
            return self._calculate_values[name](to_calculate_raw_data)
        except KeyError:
            raise FormulaToCalculateNotFoundError
