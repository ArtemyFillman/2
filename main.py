# 1
def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Пример использования функции
a = 5
b = 10
a, b = swap_values(a, b)
print("a =", a)  # Выводит: a = 10
print("b =", b)  # Выводит: b = 5

#2
def swap_values(a, b):
    a, b = b, a
    return a, b


a = 'x'
b = 'y'
a, b = swap_values(a, b)
print("a =", a)  # Выводит: a = y
print("b =", b)  # Выводит: b = x

# 3
def calculate_tax(oklad, procent):
    nalog = oklad * procent / 100
    summa = oklad - nalog
    return nalog, summa

# Пример использования функции
oklad = 50000
procent = 20
nalog, summa = calculate_tax(oklad, procent)
print("Размер подоходного налога:", nalog)
print("Сумма, получаемая на руки:", summa)

#4
def convert_weight(weight):
    kilograms = weight / 1000
    tonnes = weight / 1000000
    return kilograms, tonnes

# Пример использования функции
weight_in_grams = 1500
kilograms, tonnes = convert_weight(weight_in_grams)
print("Вес в килограммах:", kilograms)
print("Вес в тоннах:", tonnes)

#5
def convert_bytes_to_kb_mb_gb(bytes):
    kilobytes = bytes / 1024
    megabytes = bytes / (1024 * 1024)
    gigabytes = bytes / (1024 * 1024 * 1024)
    return kilobytes, megabytes, gigabytes

# Пример использования функции
bytes = 1024000
kilobytes, megabytes, gigabytes = convert_bytes_to_kb_mb_gb(bytes)
print("Объем информации в килобайтах:", kilobytes)
print("Объем информации в мегабайтах:", megabytes)
print("Объем информации в гигабайтах:", gigabytes)

#6
def check_grade(P):
    if P == 5:
        s = "Молодец!"
    elif P == 4:
        s = "Хорошо!"
    elif P <= 3:
        s = "Лентяй!"
    else:
        s = "Некорректное значение P"
    return s

# Ввод значения P с клавиатуры
P = int(input("Введите значение P: "))

# Проверка значения P и формирование строки s
s = check_grade(P)
print(s)

#7
def check_number(num):
    if num % 2 == 0 and num % 4 == 0:
        return "Число является четным и кратным 4."
    else:
        return "Число не является четным и кратным 4."

# Ввод натурального числа с клавиатуры
num = int(input("Введите натуральное число: "))

# Проверка числа и вывод результата
result = check_number(num)
print(result)

#8
def check_number(num):
    if num % 2 != 0 and num % 5 == 0:
        return "Число является нечетным и кратным 5."
    else:
        return "Число не является нечетным и кратным 5."

# Ввод натурального числа с клавиатуры
num = int(input("Введите натуральное число: "))

# Проверка числа и вывод результата
result = check_number(num)
print(result)

#9
def check_range(x, a, b):
    if x >= a and x <= b:
        return "Число принадлежит заданному промежутку."
    else:
        return "Число не принадлежит заданному промежутку."

# Ввод числа X, а и b с клавиатуры
x = float(input("Введите число X: "))
a = float(input("Введите начало промежутка a: "))
b = float(input("Введите конец промежутка b: "))

# Проверка числа и вывод результата
result = check_range(x, a, b)
print(result)

#10
import math

def calculate_z(x, y):
    if x > y:
        z = math.sqrt(x * y)
    else:
        z = math.log(x + y)
    return z

# Ввод чисел X и Y с клавиатуры
x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))

# Вычисление Z и вывод результата
z = calculate_z(x, y)
print("Значение Z =", z)