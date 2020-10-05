while True:
    try:
        first_number = float(input('Enter first number: '))
        second_number = float(input('Enter second number: '))
        sign = input('Enter sign: ')
        if sign in ['/', '*', '-', '+']:
            if sign == '+':
                print(first_number + second_number)
            elif sign == '-':
                print(first_number - second_number)
            elif sign == '*':
                print(first_number * second_number)
            elif sign == '/':
                if second_number != 0:
                    print(first_number / second_number)
                else:
                    print('ZeroDivision')
        elif sign == '0':
            print('Exit')
            break
        else:
            print('Wrong sign')
    except ValueError:
        print('ValueError')
