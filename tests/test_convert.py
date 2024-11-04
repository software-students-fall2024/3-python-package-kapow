import pytest
from pyanimalconverter import convert
from pint import *

ureg = UnitRegistry()
Q_ = ureg.Quantity

def test_sanity_check():
    """
    Test debugging... making sure that we can run a simple test that always passes.
    Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
    From the main project directory, run the `python3 -m pytest` command to run all tests.
    """
    expected = True  # the value we expect to be present
    actual = True  # the value we see in reality
    assert actual == expected, "Expected True to be equal to True!"

def test_another_true():
    assert True

def test_convert_diff_compatible_units():
    quantity = convert.convert(1, "km", "m")
    assert quantity.magnitude == 1000
    assert quantity.units == "meter"

def test_convert_diff_incompatible_units():
    with pytest.raises(DimensionalityError):    # pint raises this Dimens Err. when you try to convert incompatible units; tests passes if our convert function raises it too
        quantity = convert.convert(1, "km", "lb")

def test_convert_same_units():
    quantity = convert.convert(1, "km", "km")
    assert quantity.magnitude == 1
    assert quantity.units == "kilometer"

