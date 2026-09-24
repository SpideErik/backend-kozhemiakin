import pytest

from app.utils.formatter import format_average


def test_format():
    assert format_average(4.4) == "Средний результат: 4.40"
