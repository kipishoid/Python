# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

from random import randint

k = 2
factor = [randint(0, 100) for i in range(k + 1)]
print(factor)
result = []
for coeff in factor:
    if coeff:
        coeff = coeff if k == 0 else '' if coeff == 1 else coeff
        degree = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        temp = f'{coeff}{degree}'
        result.append(temp)
    k -= 1
polynom = ' + '.join(result) + ' = 0'
print(polynom)

with open('polynom.txt', 'w', encoding='utf-8') as file:
    file.write(polynom)
