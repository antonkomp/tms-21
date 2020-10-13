number = None
while number != 0:
    print('''Please enter the number to:
    1 - Convert inches to centimeters.
    2 - Convert centimeters to inches.
    3 - Convert miles to kilometers.
    0 - Exit.''')

    number = int(input())

    if number == 1:
        def inch_to_centimeter(inches):
            cent = inches * 2.54
            return cent

        input_inches = int(input())
        centimeters = inch_to_centimeter(input_inches)
        print(centimeters)

    elif number == 2:
        def centimeter_to_inch(cent):
            inch = cent / 2.54
            return inch

        input_centimeters = int(input())
        inch = centimeter_to_inch(input_centimeters)
        print(inch)

    elif number == 3:
        def mile_to_km(miles):
            km = miles * 1.60934
            return km

        input_miles = int(input())
        km = mile_to_km(input_miles)
        print(km)

    elif number == 0:
        break

