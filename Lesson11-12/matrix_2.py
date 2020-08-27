from random import randint

m = int(input('Please enter size matrix: '))

lst = [[randint(10, 50) for _ in range(m)] for _ in range(m)]


def print_matrix(matrix):
    tmp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:>4}'.format(matrix[i][j]), end='')
            tmp[j] += matrix[i][j]
        print()
    print()

    for i in range(len(tmp)):
        print('{:>4}'.format(tmp[i]), end='')
    print()
    print()


def sort_matrix(matrix):
    tmp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            tmp[j] += matrix[i][j]

    for i in range(len(tmp) - 1):
        for j in range(len(tmp) - 1 - i):
            if tmp[j] > tmp[j+1]:
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
                for c in range(len(matrix)):
                    matrix[c][j], matrix[c][j + 1] = matrix[c][j + 1], matrix[c][j]

    for j in range(len(matrix[0])):
        for c in range(len(matrix) - 1):
            for i in range(len(matrix) - 1 - c):
                if j % 2 == 0:
                    if matrix[i][j] < matrix[i+1][j]:
                        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                else:
                    if matrix[i][j] > matrix[i+1][j]:
                        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]


print_matrix(lst)
sort_matrix(lst)
print_matrix(lst)
