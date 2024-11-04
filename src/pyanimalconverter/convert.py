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