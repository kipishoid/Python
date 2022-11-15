# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from random import *


def input_dat(name):
    x = int(
        input(f"{name}, сколько конфет вы возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def play_print(name, a, counter, value):
    print(
        f"Ходил {name}, он взял {a}, теперь у него {counter}. На столе осталось {value} конфет.")


player1 = input("Введите имя: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        a = input_dat(player1)
        counter1 += a
        value -= a
        flag = False
        play_print(player1, a, counter1, value)
    else:
        a = randint(1, 29)
        counter2 += a
        value -= a
        flag = True
        play_print(player2, a, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
