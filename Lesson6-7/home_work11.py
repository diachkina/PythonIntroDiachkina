h = int(input())
w = h * 2 - 1

for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if i == h - 1 or j == w // 2 + i or j == w // 2 - i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()


for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if i <= h - 1 and j <= w // 2 + i and j >= w // 2 - i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

w = h
for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j == w // 2 + h - i - 1 or j == w // 2 - h + i + 1:
            print('* ', end='')
        elif i <= h // 2 and j <= w // 2 + i and j >= w // 2 - i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()


for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j == w // 2 + h - i - 1 or j == w // 2 - h + i + 1 or j == w // 2:
            print('* ', end='')
        elif i <= h // 2 and j <= w // 2 + i and j >= w // 2 - i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()