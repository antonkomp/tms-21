from random import randint

start_number = randint(50, 150)
S = 0
for i in range(1, start_number):
    S += 1 / i
print(f'N = {start_number}, sum = {S}')