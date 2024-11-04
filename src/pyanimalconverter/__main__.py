import sys
import pyanimalconverter.convert as convert
import pyanimalconverter.minmax as minmax
import pyanimalconverter.conversation as conversation



def main():
    args = convert.parse_main_args(sys.argv[1:])
    if args.operation == 'compare':
        convert.compare(args.num1, args.num2, args.unit1, args.unit2)
    elif args.operation == 'convert':
        convert.convert(args.num1, args.from_unit, args.to_unit)
    elif args.operation == 'help':
        pass
        if args.help_subcommand == "units":
            convert.print_units()
    return args

if __name__ == "__main__":
    main()