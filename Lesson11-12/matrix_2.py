from random import randint

C = R = int(input("Enter the number more than 5: "))

matrix = [[randint(1, 50) for _ in range(C)] for _ in range(R)]
# print(matrix)

total_C = [0] * C
for i in range(R):
    # total_R = 0
    for j in range(C):
        # total_R += matrix[i][j]
        total_C[j] += matrix[i][j]
        print('{:<5}'.format(matrix[i][j]), end='')
    print()

for i in total_C:
    print('{:<5}'.format(i), end='')

print()


def bubble_sort(array):
    for i in range(len(array) - 1):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False

        if flag:
            break
    print()


bubble_sort(total_C)
print(total_C)

# for i in range(R):
#     for j in range(C):
#         print('{:<5}'.format(matrix[i][j]), end='')
#     print()


