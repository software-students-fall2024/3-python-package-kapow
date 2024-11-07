from pyanimalconverter import minmax, convert
import sys

# #want to find the minimum
# print(minmax.min(["1 in", "3 in", "5 in", "6 in"])) # 1 in
# print(minmax.max(["1 in", "3 in", "5 in", "6 in"])) # 6 in

# print(minmax.min(["24 in", "1 ft", "50 in", "3 ft"])) # 1 ft
# print(minmax.max(["24 in", "1 ft", "50 in", "3 ft"])) # 50 in

# print(minmax.min(["0.01 km", "10 m", "1000 cm"])) #.01 km
# print(minmax.min(["10 m", "0.01 km", "1000 cm"])) # 10 m
# print(minmax.max(["0.01 km", "10 m", "1000 cm"]))

# print(minmax.min(["1 in", "1 in", "1 in", "1 in"]))
# print(minmax.max(["1 in", "1 in", "1 in", "1 in"]))

# print(convert.convert(12, "in", "ft"))
# print(convert.convert(6, "ft", "m")) #about 2

# try:
#     print(convert.convert(19, "chickens", "cows")) #-1
#     print(convert.convert(8, "lb", "km")) #-2
# except SystemExit:
#     print("Caught error, carrying on")

# print("Running the exception")

# try:
#     print(minmax.min([])) #will raise SystemExit(1)
# except SystemExit:
#     print("Correct Error Thrown")

# print("Carrying on now")
# print("Hello there"
print("Apple", file = sys.stderr)
sys.exit(1)
'''
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
'''