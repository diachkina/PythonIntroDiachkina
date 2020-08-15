n = input()


def blablabla():
    q = list(enumerate(map(int, str(n)), 1))
    y = sum(list(map(lambda x: x[0]*x[1], q)))
    print(q)
    return y


print("Total: ", blablabla())
