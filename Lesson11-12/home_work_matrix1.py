from random import randint

rows = int(input())
cols = int(input())

matrix = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]

# print(matrix)
# print()

for i in range(rows):
    total_rows = 0
    for j in range(cols):
        total_rows += matrix[i][j]
        print('{:<5}'.format(matrix[i][j]), end='')
    print(" ", total_rows)
print()

total_cols = [0] * cols
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        total_cols[col] += matrix[row][col]

#print('{:>3}'.format(list(total_cols)), end='')
print(total_cols, end='')

# for line in rating:
#     line = line.split(', ')[1: -2]
#     for idx in range(len(line)):
#         matrix[idx] += int(line[idx]
