n = int(input("Введите натуральное число: "))
p_st, st2 = 0, 1
while st2 <= n:
    st2 *= 2
    p_st += 1
print(p_st - 1, st2 // 2)