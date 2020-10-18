from random import randint

list_number = [randint(0, 100) for i in range(19)]
max_number = max(list_number)
for id, item in enumerate(list_number):
    if item % 2 == 0:
        list_number.remove(item)
        list_number.insert(id, max_number)

print(list_number, max_number)
