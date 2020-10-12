from random import randint

list_number = [randint(0, 100) for i in range(100)]
counter = 0
for i in range(len(list_number)):
    if i == len(list_number) - 2:
        if list_number[-1] > list_number[-2]:
            counter += 1
        break
    elif list_number[i] < list_number[i + 1] > list_number[i + 2]:
        counter += 1
print(counter)
print(list_number)
