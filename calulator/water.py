import attr
from common.constants import *

DEFAULT_MALT_TAKES = 1 / 1  # количество литров, сколько в себя впитает солод
DEFAULT_SEDIMENT = liters(2.5)  # осадок несмываемый + остаточные продукты от солода
DEFAULT_BOILING_PERCENT = 0.15  # количество выкипаемой воды в %


@attr.s
class WaterInfo(object):
    total = attr.ib(type=int)
    input = attr.ib(type=int)
    flush = attr.ib(type=int)


def calculate(expected_ml: int,
              hydro_module: float,
              malt_mass: int,
              malt_takes: float = DEFAULT_MALT_TAKES,
              sediment_ml: int = DEFAULT_SEDIMENT,
              boiling_percent: float = DEFAULT_BOILING_PERCENT
              ) -> WaterInfo:
    v_total = expected_ml + malt_mass * malt_takes + sediment_ml
    v_total *= (1 + boiling_percent)
    v_total = int(v_total)

    v_input = int(malt_mass / hydro_module)
    v_flush = int(v_total - v_input)
    assert v_flush > 0, "Incorrect arguments. Couldn't calculate positive flush volume"
    return WaterInfo(v_total, v_input, v_flush)
