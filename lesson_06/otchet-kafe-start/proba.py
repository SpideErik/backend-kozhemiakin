import os

from app.utils.formatter import format_title
from app.utils.text import _squash_spaces
from app.services import calculator


def total(prices: list[int]) -> int:
    return sum(prices)


def pick(flag: bool) -> str:
    if flag:
        label = "есть выручка"
    return label


heading = format_title("test", 40)
clean = _squash_spaces("иванов   пётр")
print(clean)

calculator.calculate_average([1,2,3,4,5])
