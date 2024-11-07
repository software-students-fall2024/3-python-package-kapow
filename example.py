from pyanimalconverter import minmax, convert
import sys

# #want to find the minimum
print(minmax.min(["1 in", "3 in", "5 in", "6 in"])) # 1 in
print(minmax.max(["1 in", "3 in", "5 in", "6 in"])) # 6 in

print(minmax.min(["24 in", "1 ft", "50 in", "3 ft"])) # 1 ft
print(minmax.max(["24 in", "1 ft", "50 in", "3 ft"])) # 50 in

print(minmax.min(["0.01 km", "10 m", "1000 cm"])) #.01 km
print(minmax.min(["10 m", "0.01 km", "1000 cm"])) # 10 m
print(minmax.max(["0.01 km", "10 m", "1000 cm"]))

print(minmax.min(["1 in", "1 in", "1 in", "1 in"]))
print(minmax.max(["1 in", "1 in", "1 in", "1 in"]))

print(convert.convert(12, "in", "ft"))
print(convert.convert(6, "ft", "m")) #about 2

try:
    print(convert.convert(19, "chickens", "cows")) #-1
    print(convert.convert(8, "lb", "km")) #-2
except SystemExit:
    print("Caught error, carrying on")

print("Running the exception")

try:
    print(minmax.min([])) #will raise SystemExit(1)
except SystemExit:
    print("Correct Error Thrown")

print("Carrying on now")


print(convert.compare(3.0, 2.0, "ft", "ft")) # 1
print(convert.compare(1.0, 12.0, "ft", "in")) # 0
print(convert.compare(5.0, 2.0, "ft", "m")) #-1