print("Координаты первой клетки")
x1 = input("Введите горизонтальную координату: ")
y1 = input("Введите вертикальную координату: ")
x1 = int(x1)
y1 = int(y1)
if 1 <= x1 <= 8 and 1 <= y1 <= 8:
    print("Координаты второй клетки")
else:
    print("Неверные координаты")
x2 = input("Введите горизонтальную координату: ")
y2 = input("Введите вертикальную координату: ")
x2 = int(x2)
y2 = int(y2)
if x2 == x1 + 2 and y2 == y1 + 1:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 + 2 and y2 == y1 - 1:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 - 2 and y2 == y1 + 1:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 - 2 and y2 == y1 - 1:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 + 1 and y2 == y1 + 2:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 + 1 and y2 == y1 - 2:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 - 1 and y2 == y1 + 2:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
elif x2 == x1 - 1 and y2 == y1 - 2:
    print("Конь МОЖЕТ попасть на вторую клетку за один ход")
else:
    print("Конь НЕ МОЖЕТ попасть на вторую клетку за один ход")