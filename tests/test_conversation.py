import pytest, sys
from pyanimalconverter.conversation import *

#custom fixture for input files
# @pytest.fixture
# def getInput():
#     file = open("convInput.txt")
#     return file.read()

# def test_unit_error(capfd, getInput):
#     sys.stdin = getInput
#     with pytest.raises(SystemExit):
#         askAnimal()
#     result = capfd.readouterr()
#     assert result == "Unit is not valid!\n"