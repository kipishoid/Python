# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.


import re

s = '(1+2)*3'

s2 = re.findall(r'\d+|[()+\-*\/]', s)
print(s2)


def operation(s2):
    oper = {'+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b}

    for i in range(s2.count('*') + s.count('/')):
        for elem in s2:
            if str(elem) in '*/':
                idx = s2.index(elem)
                result = oper[elem](float(s2[idx - 1]), float(s2[idx + 1]))
                s2[idx - 1: idx + 2] = [result]

    for i in range(s2.count('+') + s.count('-')):
        for elem in s2:
            if str(elem) in '+-':
                idx = s2.index(elem)
                result = oper[elem](float(s2[idx - 1]), float(s2[idx + 1]))
                s2[idx - 1: idx + 2] = [result]

    return s2


for j in range(s2.count('(')):
    if '(' in s2:
        op = s2.index('(')
        cl = s2.index(')')
        res = s2[op+1:cl]
        operation(res)
        s2[op:cl+1] = res

operation(s2)
print(s2[0])
