# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.


string1 = 'пользователь должен написать программу, в которой пользователь будет задавать две строки, пользователь'
string2 = 'пользователь'
count_o = 0
for i in range(len(string1)):
    if string2 in string1[i: i + len(string2)]:
        count_o += 1
print(count_o)
