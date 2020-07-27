from random import randint
lst = [randint(1, 100) for _ in range(10)]
print(lst)
lst.append(0)
k = int(input("Enter the index: "))
c = int(input("Enter the value: "))
for ind in range(len(lst) - 1, k, -1):
    lst[ind] = lst[ind - 1]
lst[k] = c
print(lst)