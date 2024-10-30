import argparse
import sys

# Unfinished list of accepted units
CHOICES = {"km", "kilometers", "mi", "miles", "lb", "pounds", "kg", "kilograms"}

# parses the arguments of the command
def parse_args(args):
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="operation", required=True)
    help_parser = subparsers.add_parser("help", help="Show verbose help instructions")

    # Write the flags for the compare function
    compare_parser = subparsers.add_parser("compare", help="Compare two values by units")
    compare_parser.add_argument(
        'num1', 
        nargs=1, 
        type=float, 
        metavar="num1",
        help="Value of first unit to compare",
    )
    compare_parser.add_argument(
        'num2', 
        nargs=1, 
        type=float, 
        metavar="num2",
        help="Value of second unit to compare",
    )
    compare_parser.add_argument(
        'unit1',
        nargs=1,
        choices=CHOICES,
        metavar="unit1",
        help="Unit of first number (run `help` to see units)",
    )
    compare_parser.add_argument(
        'unit2',
        nargs=1,
        choices=CHOICES,
        metavar="unit2",
        help="Unit of second number (run `help` to see units)",
    )

    convert_parser = subparsers.add_parser("convert", help="Convert a value to another unit")
    convert_parser.add_argument(
        'num1',
        nargs=1,
        type=float,
        help="Value of unit to convert",
    )
    convert_parser.add_argument(
        'from_unit',
        nargs=1,
        choices=CHOICES, 
        metavar='from_unit',
        help="Unit given input value",
    )
    convert_parser.add_argument(
        'to_unit',
        nargs=1,
        choices=CHOICES,
        metavar='to_unit',
        help="Unit of desired output value",
    )

    args = parser.parse_args(args)
    if args.operation == 'compare':
        print(args)
    elif args.operation == 'convert':
        print(args)
    elif args.operation == 'help':
        print("RUN HELP COMMAND HERE")
    return args