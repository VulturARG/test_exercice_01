from inspect import getmembers, isclass, isabstract
import app.calculated_values as formulas_package
from app.sensors_procesing import ToCalculateRawData, FormulaToCalculateNotFoundError, \
    SensorValueIsNoneError


class CalculateValueFactory:
    """Get an instance of the right class."""

    calculate_values = {}  # key = sensor type, Value = class for the calculate

    def __init__(self):
        self._load_calculation_formulas()

    def _load_calculation_formulas(self) -> None:
        """Populate the calculate_values dictionary with classes of calculate_values package"""

        classes = getmembers(
            formulas_package,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, formulas_package.CalculateValue):
                self.calculate_values.update([[name, _type]])

    def create_instance(self, to_calculate_raw_data: ToCalculateRawData) -> calculate_values:
        """Create the solicited instance."""

        name = to_calculate_raw_data.config.type

        try:
            return self.calculate_values[name](to_calculate_raw_data)
        except KeyError:
            raise FormulaToCalculateNotFoundError
