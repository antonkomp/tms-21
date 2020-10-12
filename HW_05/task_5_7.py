import random

size_matrix = 7
matrix = [[random.randint(10, 50) for j in range(size_matrix)] for i in range(size_matrix)]
for i in range(size_matrix):
    for j in range(size_matrix):
        if i == j:
            matrix[i][j] = max(matrix[i])
        print(matrix[i][j], end=' ')
    print()
