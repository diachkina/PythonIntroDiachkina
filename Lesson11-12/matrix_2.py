from random import randint

C = R = int(input("Enter the number more than 5: "))

matrix = [[randint(1, 50) for _ in range(C)] for _ in range(R)]
print(matrix)

total_C = [0] * C
for i in range(R):
    # total_R = 0
    for j in range(C):
        # total_R += matrix[j][i]
        total_C[j] += matrix[i][j]
        print('{:<5}'.format(matrix[i][j]), end='')
    # print(" ", total_R)
    print()
for i in total_C:
    print('{:<5}'.format(i), end='')

print()

for j in range(len(matrix) - 1):
    flag = True
    for i in range(len(matrix) -1-j):
        if sum(matrix[j])>sum(matrix[j+1]):
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
            flag = False
        if flag:
            break
    print()
for i in range(C):
    for j in range(R):
        print('{:<5}'.format(matrix[i][j]), end='')
    print()




# print()

#
# bubble_sort(matrix)
# print(matrix)

# for i in range(C):
#     for j in range(R):
#         print('{:<5}'.format(matrix[j][i]), end='')
#     print()

# print(matrix)
