import random

# 1 task
start_num = 10
end_num = 90
matrix_row = 5
matrix_col = 5

matrix = [[random.randint(start_num, end_num) for j in range(matrix_col)] for i in range(matrix_row)]
for i in range(matrix_row):
    for j in range(matrix_col):
        print(matrix[i][j], end=' ')
    print()
print()


# 2 task
def max_el(matrix):
    return max(map(max, matrix))


max_elem = max_el(matrix)
print('max element:', max_elem)
print()


# 3 task
def min_el(matrix):
    return min(map(min, matrix))


min_elem = min_el(matrix)
print('min element:', min_elem)
print()

# 4 task
sum = 0
for i in range(matrix_row):
    for j in range(matrix_col):
        sum += matrix[i][j]
print('sum elements:', sum)
print()