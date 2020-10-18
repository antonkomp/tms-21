number_from = int(input())
number_to = int(input())
for item in range(number_from, number_to + 1):
    print(f'{item}:', end=' ')
    for i in range(2, item):
        if item % i == 0:
            print(item // i, end=' ')
    print()
