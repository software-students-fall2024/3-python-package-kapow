import sys
from . import convert


def main():
    args = convert.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()