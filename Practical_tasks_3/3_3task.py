# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

list_a = [1.1, 1.2, 3.1, 5, 10.01]
max = 0
min = 1
for i in list_a:
    a = i - int(i)
    if a > max:
        max = a
    if a < min:
        min = a
print(f'{list_a}', ' => ', round(max-min, 3))
