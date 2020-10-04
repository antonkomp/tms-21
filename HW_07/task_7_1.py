def inch_to_centimeter(inches):
    cent = inches * 2.54
    return cent


def centimeter_to_inch(cent):
    inch = cent / 2.54
    return inch


def mile_to_km(miles):
    km = miles * 1.60934
    return km


input_inches = int(input())
centimeters = inch_to_centimeter(input_inches)
print(centimeters)

input_centimeters = int(input())
inch = centimeter_to_inch(input_centimeters)
print(inch)

input_miles = int(input())
km = mile_to_km(input_miles)
print(km)
