# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint as rnd

number_list = [rnd(2, 10) for i in range(int(input("Количество элементов? ")))]
print(number_list)
print(
    [
        number_list[i] * number_list[-(i + 1)]
        for i in range(len(number_list) // 2 + len(number_list) % 2)
    ]
)
