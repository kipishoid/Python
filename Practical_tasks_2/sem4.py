# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# *Пример: *

# - для k = 8 список будет выглядеть так:
# [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21][Негафибоначчи]


# num = int(input('Введите целое число: '))
# list_pos = [0, 1]
# list_neg = [0, 1]
# for i in range(num - 1):
#     list_pos.append(list_pos[-1] + list_pos[-2])
#     list_neg.append(list_neg[-2] - list_neg[-1])
# list_result = list_neg[::-1] + list_pos[1:]
# print(list_result)


# решение 2
# num = int(input("Введите количество членов ряда Негафибоначчи: "))
# result = [1, 0, 1]
# while num != 1:
#     k = (result[-1]+result[-2])
#     result.append(k)
#     result.insert(0, (-1)**(num+1)*k)
#     num -= 1
# print(result)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0)
# с помощью математических формул нахождения корней
# квадратного уравнения

# a = int(input('Введите значение a: '))
# b = int(input('Введите значение b: '))
# c = int(input('Введите значение c: '))
# a = float(a)
# b = float(b)
# c = float(c)
# discriminant = b**2 - 4*a*c
# print('Дискриминант = ' + str(discriminant))
# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print('x = ' + str(x))
# else:
#     x1 = (-b + discriminant ** 0.5) / (2 * a)
#     x2 = (-b - discriminant ** 0.5) / (2 * a)
#     print('x₁ = ' + str(x1))
#     print('x₂ = ' + str(x2))


# 3. Задайте два числа. Напишите программу,
# которая найдёт НОК(наименьшее общее кратное) этих двух чисел.


x = int(input("Введите первое число для нахождения наименьшего общего кратного: "))
y = int(input("Введите второе число для нахождения наименьшего общего кратного: "))

big_num = max(x, y)

while True:
    if (big_num % x == 0) and (big_num % y == 0):
        result = big_num
        break
    big_num += 1
print(result)
