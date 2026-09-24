import pytest

from app.services.calculator import calculate_average

def test_average():
    assert calculate_average([5, 4, 5, 3, 5]) == pytest.approx(4.4)


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
