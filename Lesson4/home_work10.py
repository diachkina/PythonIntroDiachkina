n = int(input())
kol = sUm = kol2 = kol1 = 0
mAx = mIn = n
while n != 0:
    kol += 1
    sUm += n
    n = int(input())
    for i in range(1, n):
        if n > mAx:
            mAx = n
        if n < mIn:
            mIn = n
    if n % 2 == 0:
        kol2 += 1
    else:
        kol1 += 1
print("Кол-во эл-в:", kol)
print("Сумма:", sUm)
print("Среднее арифметическое:", sUm / kol)
print("Мах", mAx)
print("Min:", mIn)
print("Кол-во нечётных:", kol1)
print("Кол-во чётных:", kol2)

# при вводе одних нечётных не работает их кол-во.
# их на 1 меньше, а в чётных 1.что я сделала неправильно?