import pytest

from src.pyanimalconverter.minmax import max

def test_all_equal():
    #ensure that when they are all equal same result is given
    inputs = ["4 ft", "48 in", "121.92 ft", "48 in"]
    assert max(inputs) == "4 ft"
    assert max(["5 in", "5 in", "5 in", "5 in"]) == "5 in"

def test_sequence():
    inputs = ["1 in", "2 in", "3 in", "4 in", "5 in"]
    assert max(inputs) == "5 in"

def test_diff():
    input1 = ["24 in", "48 in", "4 ft", "0.6 m", "0.0004 km"]
    input2 = ["2 ft", "4 ft", "48 in", "0.6 m", "0.0004 km"]
    input3 = ["24 in", "42 in", "1 ft", "0.1 m", "4 km"]

    assert max(input1) == "48 in"
    assert max(input2) == "4 ft"
    assert max(input3) == "4 km"

def test_errors():
    assert max(["2 in", "8 in", "5 lb"]) == -2
    assert max(["4 nm", "2 in", "8 in"]) == -1

def test_empty():
    with pytest.raises(SystemExit(1)):
        max([])