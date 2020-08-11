lst = [
    [12345, "python 1", 4, 40.95],
    [12346, "python 2", 6, 56.80],
    [12347, "python 3", 3, 32.95],
    [12348, "python 4", 3, 24.99]
]


def answer():
    # res = tuple(map(lambda x: x[2] * x[3] if x[2] * x[3] >= 100 else x[2] * x[3] + 10, lst))
    # res2 = tuple(map(lambda x: x[0], lst))
    # return list(map(lambda q, w: (q, w), res, res2))

    # return list(map(lambda q, w: (q, w),
    #                 tuple(map(lambda x: x[0], lst)),
    #                 tuple(map(lambda x: x[2] * x[3] if x[2] * x[3] >= 100 else x[2] * x[3] + 10, lst))))

    return list(zip(tuple(map(lambda x: x[0], lst)),
                    tuple(map(lambda x: x[2] * x[3] if x[2] * x[3] >= 100 else x[2] * x[3] + 10, lst))))


print(answer())
