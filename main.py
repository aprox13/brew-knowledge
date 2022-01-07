from calulator.water import calculate
from common.constants import *


if __name__ == '__main__':
    print(calculate(
        expected_ml=liters(27),
        hydro_module=1/4,
        malt_mass=kg(6)
    ))