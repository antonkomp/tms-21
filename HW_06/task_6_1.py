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

# 5 task
max_sum_row = 0
var_sum = 0
index = 0
for i in range(matrix_row):
    for j in range(matrix_col):
        var_sum += matrix[i][j]
    if max_sum_row < var_sum:
        max_sum_row = var_sum
        index = i
    var_sum = 0
print(f'index max sum row: {index} ({max_sum_row})')

# 6 task
var_sum = [0 for x in range(matrix_col)]
for i in range(matrix_row):
    for j in range(matrix_col):
        var_sum[j] += matrix[i][j]
max_sum_col = max(var_sum)
index = var_sum.index(max_sum_col)
print(f'index max sum col: {index} ({max_sum_col})')

# 7 task
var_sum = 0
var_sum_arr = []
for i in range(matrix_row):
    for j in range(matrix_col):
        var_sum += matrix[i][j]
    var_sum_arr.append(var_sum)
    var_sum = 0
min_sum_row = min(var_sum_arr)
index = var_sum_arr.index(min_sum_row)
print(f'index min sum row: {index} ({min_sum_row})')

# 8 task
var_sum = [0 for x in range(matrix_col)]
for i in range(matrix_row):
    for j in range(matrix_col):
        var_sum[j] += matrix[i][j]
min_sum_col = min(var_sum)
index = var_sum.index(min_sum_col)
print(f'index min sum col: {index} ({min_sum_col})')

# 9 task
for i in range(matrix_row):
    for j in range(matrix_col):
        if i < j:
            matrix[i][j] = 0
        print("{:>3}".format(matrix[i][j]), end='')
    print()
print()

# 10 task
for i in range(matrix_row):
    for j in range(matrix_col):
        if i > j:
            matrix[i][j] = 0
        print("{:>3}".format(matrix[i][j]), end='')
    print()
print()

# 11 task
print('New 2 matrix:')
matrix_a = [[random.randint(start_num, end_num) for j in range(matrix_col)] for i in range(matrix_row)]
for i in range(matrix_row):
    for j in range(matrix_col):
        print(matrix_a[i][j], end=' ')
    print()
print()

matrix_b = [[random.randint(start_num, end_num) for j in range(matrix_col)] for i in range(matrix_row)]
for i in range(matrix_row):
    for j in range(matrix_col):
        print(matrix_b[i][j], end=' ')
    print()
print()
