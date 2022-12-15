# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

from random import uniform as rnd


def rub(n):
    return n % 1


number_list = [
    round(rnd(1, 10), 2) for i in range(int(input("Количество элементов? ")))
]
print(number_list)
j = 0
while j < len(number_list):
    if rub(number_list[j]) == 0:
        del number_list[j]
    else:
        j += 1
maxim = max(number_list, key=rub)
print(f"С максимальной дробной частью: {maxim}")
minim = min(number_list, key=rub)
print(f"С минимальной дробной частью: {minim}")
print(f"Разница: {round(rub(maxim - minim),2)}")
