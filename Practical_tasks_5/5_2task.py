# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('text_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст для кодировки: '))
with open('text_RLE.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()
print(my_text)


def compress(txt):
    compression = ''
    prev = ''
    count = 1
    if not txt:
        return ''

    for i in txt:
        if i != prev:
            if prev:
                compression += str(count) + prev
            count = 1
            prev = i
        else:
            count += 1
    else:
        compression += str(count) + prev
        return compression


text_compression = compress(my_text)

with open('text_compression_RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)
