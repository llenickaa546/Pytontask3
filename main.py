# 4.1 Проверка пароля
p1 = input("Введите пароль: ")
p2 = input("Повторите пароль: ")

if p1 == p2:
    print("Пароль принят")
else:
    print("Пароль не принят")

# 4.2 Места в поезде
seat = int(input("Введите номер места: "))

if 1 <= seat <= 36:
    if seat % 2 == 0:
        print("Верхнее место в купе")
    else:
        print("Нижнее место в купе")
elif 37 <= seat <= 54:
    if seat % 2 == 0:
        print("Верхнее боковое")
    else:
        print("Нижнее боковое")
else:
    print("Ошибка")

# 4.3 Високосный год
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Не високосный")

# 4.4 Смешивание цветов
c1 = input("Цвет 1: ").lower()
c2 = input("Цвет 2: ").lower()

colors = ["красный", "синий", "желтый"]

if c1 not in colors or c2 not in colors:
    print("Ошибка")
elif c1 == c2:
    print(c1)
elif (c1 == "красный" and c2 == "синий") or (c1 == "синий" and c2 == "красный"):
    print("Фиолетовый")
elif (c1 == "красный" and c2 == "желтый") or (c1 == "желтый" and c2 == "красный"):
    print("Оранжевый")
elif (c1 == "синий" and c2 == "желтый") or (c1 == "желтый" and c2 == "синий"):
    print("Зеленый")
