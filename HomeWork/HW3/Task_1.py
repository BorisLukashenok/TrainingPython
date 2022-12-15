# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции

from random import randint as rnd

number_list = [rnd(0, 10) for i in range(int(input("Количество элементов? ")))]
print(number_list)
print(f"Сумма элементов на нечетной позиции: {sum(number_list[1::2])}")
