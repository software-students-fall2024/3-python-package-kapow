import pytest

from pyanimalconverter import minmax

def test_all_equal():
    #ensure that when they are all equal same result is given
    inputs = ["4 ft", "48 in", "121.92 cm", "48 in"]
    assert minmax.min(inputs) == "4 ft"
    assert minmax.min(["5 in", "5 in", "5 in", "5 in"]) == "5 in"

def test_sequence():
    inputs = ["1 in", "2 in", "3 in", "4 in", "5 in"]
    assert minmax.min(inputs) == "1 in"

def test_diff():
    input1 = ["24 in", "42 in", "1 ft", "60 m", "4 km"]
    input2 = ["2 ft", "42 in", "12 in", "60 m", "4 km"]
    input3 = ["24 in", "42 in", "1 ft", "0.1 m", "4 km"]

    assert minmax.min(input1) == "1 ft"
    assert minmax.min(input2) == "12 in"
    assert minmax.min(input3) == "0.1 m"

def test_errors():
    assert minmax.min(["2 in", "8 in", "5 lb"]) == -2
    assert minmax.min(["4 nm", "2 in", "8 in"]) == -1

def test_empty():
    with pytest.raises(SystemExit):
        minmax.min([])