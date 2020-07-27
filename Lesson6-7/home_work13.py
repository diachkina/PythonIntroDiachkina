from random import randint
lst = [randint(1, 100) for _ in range(10)]
print(lst)
# lst.append(0)
# print(lst)
k = int(input("Enter the index: "))
c = int(input("Enter the value: "))
# lst[k] = c
for ind in range(k, len(lst)-1):
    lst[ind] = lst[ind - 1]
print(lst)