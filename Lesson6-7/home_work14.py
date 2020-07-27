from random import randint
lst1 = [randint(1, 100) for _ in range(5)]
lst1.sort()
print(lst1)
lst2 = [randint(1, 100) for _ in range(3)]
lst2.sort()
print(lst2)

ind_1 = ind_2 = 0
lst3 = []
while ind_1 < len(lst1) and ind_2 < len(lst2):
    if lst1[ind_1] < lst2[ind_2]:
        lst3.append(lst1[ind_1])
        ind_1 += 1
    else:
        lst3.append(lst2[ind_2])
        ind_2 += 1

while ind_1 < len(lst1):
    lst3.append(lst1[ind_1])
    ind_1 += 1
while ind_2 < len(lst2):
    lst3.append(lst2[ind_2])
    ind_2 += 1

print(lst3)
