from random import randint

rows = int(input())
cols = int(input())

matrix = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]
# print(matrix)

for i in range(rows):
    for j in range(cols):
        print('{:<30}'.format(matrix[i][j], end=''))
    print('')
