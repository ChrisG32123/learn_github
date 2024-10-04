# Tests from https://www.softwaretestinghelp.com/pytest-tutorial/

import pytest
from example_functions import my_adder, my_thermo_stat, have_digits, area_of_rectangle, perimeter_of_rectangle

@pytest.mark.parametrize("a,b,c,expected", [(2, 3, 5, 10), (3, 4, 5, 12), (6, 8, 10, 24)])
def test_my_adder(a, b, c, expected):
    """
    tests my_adder.

    Args:
        a: first number
        b: second number
        c: third number
        expected: expected sum
    """
    assert my_adder(a, b, c) == expected

@pytest.mark.parametrize("temp,desired_temp,desired", [(30, 20, "AC"), (20, 30, "Heat"), (20, 20, "off")])
def test_my_thermo_stat(temp, desired_temp, desired):
    """
    tests my_thermo_stat.

    Args:
        temp: temperature
        desired_temp: desired temperature
        desired: desired status
    """
    assert my_thermo_stat(temp, desired_temp) == desired

def test_have_digits():
    """
    tests have_digits.
    """
    assert have_digits("abc123") == 1

@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    """
    tests area_of_rectangle.

    Args:
        width: width
        height: height
        area: expected area
    """
    output = area_of_rectangle(width, height)
    assert output == area

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    """
    tests perimeter_of_rectangle.

    Args:
        width: width
        height: height
        perimeter: expected perimeter
    """
    output = perimeter_of_rectangle(width,height)
    assert output == perimeter
    