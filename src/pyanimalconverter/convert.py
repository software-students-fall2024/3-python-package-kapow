<<<<<<< HEAD

lengths = ["m", "in", "km", "cm", "ft"]
wieght = ["lb", "oz", "g", "kg"]

we = {
    "lb": {
        "kg": 0.453592,
        "lb": 1,
        "oz": 16,
        "g":  0.000453592
    },
    "oz": {
        "oz": 1,
        "lb": 1/16,
        "kg": 0.453592/16,
        "g": 453.592/16
    },
    "kg":{
        "kg": 1, 
        "g": 1000,
        "lb": 2.20462,
        "oz": 2.20462*16
    }, 
    "g":{
        "kg": 0.001, 
        "g": 1,
        "lb": 0.00220462,
        "oz": 0.00220462*16
    },
    "cm":{
        "cm": 1,
        "m": .01,
        "km": 0.00001,
        "ft": 0.0328084,
        "in": 0.0328084*12
    },
    "m":{
        "cm": 100,
        "m": 1,
        "km": 0.001,
        "ft": 3.28084,
        "in": 3.28084*12
    },
    "km":{
        "cm": 100000,
        "m": 1000,
        "km": 1,
        "ft": 3.28084*1000,
        "in": 3.28084*12000
    },
    "ft":{
        "cm": 30.48,
        "m": 0.3048,
        "km": 0.3048*0.001,
        "ft": 1,
        "in": 12
    },
    "in":{
        "cm": 30.48/12,
        "m": 0.3048/12,
        "km": 0.3048*0.001/12,
        "ft": 1/12.0,
        "in": 1
    }
}




def convert(num1: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in we.keys() or to_unit not in we.keys():
        return -1
    elif to_unit not in we.get(from_unit).keys():
        return -2 #incompatible
    else:
        result = num1 * we.get(from_unit).get(to_unit)
        return round(result, 2)
=======
import argparse
import sys
from pint import *
from collections import defaultdict

ureg = UnitRegistry()
ureg.formatter.default_format = '.3f'


def print_units():
    ureg = UnitRegistry()
    # Dictionary to hold units by category
    categories = defaultdict(list)

    # Group units by their dimensionality
    
    for unit in ureg._units:
        try:
            unit_obj = ureg[unit]
            dimension = str(unit_obj.dimensionality)  # Get the dimension as a string
            categories[dimension].append(unit)  # Append the unit to the appropriate category
        except:
            pass

    relevant_cats = ['[length]', '[mass]', '[time]', '[temperature]']
    # Display the units by category
    print("Units by Category:\n")
    for category, units in sorted(categories.items()):
        if category in relevant_cats:
            print(f"{category}:")
            for unit in sorted(units):
                print(f"  - {unit} ({ureg[unit]})")
            print()  # Newline for better readability

def compare(num1, num2, unit1, unit2):
    """
    Compares two quantities and returns an array of 2 PintQuantity variables with the largest being first

    Args:
        num1 (int): First value
        num2 (int): Second value
        unit1 (str): Unit of first value
        unit2 (str): Unit of seconf value

    Returns:
        list: The quantities as PintQuantity variables in descending order
    """
    quant1 = convert(num1, unit1, unit1)
    quant2 = convert(num2, unit2, unit1)
    if quant1 >= quant2:
        return [quant1, quant2]
    else:
        return [quant2, quant1]
    

def convert(num1, from_unit, to_unit):
    try:
        from_registry = ureg.parse_expression(from_unit)
        to_registry = ureg.parse_expression(to_unit)
    except Exception as e:
        print(f'Error parsing unit(s): {e}')
        sys.exit(1)
    if not from_registry.is_compatible_with(to_registry):
        print(f"Invalid conversion {from_registry.units} to {to_registry.units}")
        sys.exit(1)

    Q_ = ureg.Quantity
    quant = Q_(num1, from_registry)
    quant = quant.to(to_registry)
    return quant

# parses the arguments of the command
def parse_main_args(args):
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Parser to accept help command
    help_parser = subparsers.add_parser("help", help="Show verbose help instructions")
    help_units_parser = help_parser.add_subparsers(dest="help_subcommand")
    units_parser = help_units_parser.add_parser("units", help="Display all units")

    # Write the flags for the compare function
    compare_parser = subparsers.add_parser("compare", help="Compare two values by units")
    # Take arguments for 2 numbers and 2 units
    compare_parser.add_argument(
        'num1',  
        type=float, 
        metavar="num1",
        help="Value of first unit to compare",
    )
    compare_parser.add_argument(
        'num2', 
        type=float, 
        metavar="num2",
        help="Value of second unit to compare",
    )
    compare_parser.add_argument(
        'unit1',
        metavar="unit1",
        help="Unit of first number (run `help` to see units)",
    )
    compare_parser.add_argument(
        'unit2',
        metavar="unit2",
        help="Unit of second number (run `help` to see units)",
    )

    # Writing flags for the convert function
    convert_parser = subparsers.add_parser("convert", help="Convert a value to another unit")
    # Takes in one number and a from_unit and to_unit
    convert_parser.add_argument(
        'num1',
        type=float,
        help="Value of unit to convert",
    )
    convert_parser.add_argument(
        'from_unit',
        metavar='from_unit',
        help="Unit given input value",
    )
    convert_parser.add_argument(
        'to_unit',
        metavar='to_unit',
        help="Unit of desired output value",
    )

    args = parser.parse_args(args)

    return args
>>>>>>> main
