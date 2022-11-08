# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number = int(input('Задайте натуральное число: '))
result = []
d = 2
num = number
while d * d <= number:
    if number % d == 0:
        result.append(d)
        number //= d
    else:
        d += 1
result.append(number)
print(f'{num} = {result}')
