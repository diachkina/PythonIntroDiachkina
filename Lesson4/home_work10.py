kol = sUm = kol2 = kol1 = 0
mAx = mIn = 0
while True:
    n = int(input())
    if n == 0:
        break

    if kol == 0:
        mIn = n
        mAx = n
    kol += 1
    sUm += n

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
print("Кол-во чётных:", kol2)
print("Кол-во нечётных:", kol1)