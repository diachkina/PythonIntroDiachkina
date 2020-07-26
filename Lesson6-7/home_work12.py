from random import randint
lst = [randint(1, 100) for _ in range(10)]
print(lst)
k = int(input("Enter the index: "))
for ind in range(k, len(lst) - 1):
    lst[ind] = lst[ind + 1]
lst.pop()
print(lst)