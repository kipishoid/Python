# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


List_a = [2, 3, 4, 5, 6]

result = [List_a[i] * List_a[-1 - i] for i in range((len(List_a) + 1) // 2)]
print(f'{List_a}', ' => ', result)
