from random import randint

rows = int(input())
cols = int(input())

matrix = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]

total_cols = [0] * cols
for i in range(rows):
    total_rows = 0
    for j in range(cols):
        total_rows += matrix[i][j]
        total_cols[j] += matrix[i][j]
        print('{:<5}'.format(matrix[i][j]), end='')
    print(" ", total_rows)
print()

for i in total_cols:
    print('{:<5}'.format(i), end='')
    
