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

total_cols = []
for column in range(len(matrix[0])):
    t = 0
    for row in matrix:
        t += row[column]
    total_cols.append(t)
    # print('{:>3}'.format(list(total_cols)), end='')
print(*total_cols, end='')

# for line in rating:
#     line = line.split(', ')[1: -2]
#     for idx in range(len(line)):
#         matrix[idx] += int(line[idx])