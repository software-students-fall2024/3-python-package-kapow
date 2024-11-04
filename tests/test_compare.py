import sys
import os
import pytest

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from pyanimalconverter.convert import compare


def test_compare_identical_units():
    # Test with identical values and units
    result = compare(100, 100, "kg", "kg")
    assert result[0].magnitude == 100
    assert result[1].magnitude == 100
    assert result[0].units == result[1].units

def test_compare_different_units():
    # Test with different but compatible units
    result = compare(1, 1, "kg", "lb") # 1kg should be approx 2.20462 lb
    assert result[0].magnitude == pytest.approx(1, rel=1e-3)
    assert result[1].magnitude == pytest.approx(0.453592, rel=1e-3) # 0.453592kg = 1lb

def test_compare_incompatible_units():
    # Test with incompatible units, expecting an error
    with pytest.raises(SystemExit): 
        compare(1, 1, "m", "s")




