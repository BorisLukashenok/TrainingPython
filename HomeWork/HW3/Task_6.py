# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

from random import randint as rnd

number_list = [rnd(0, 10) for i in range(int(input("Количество элементов? ")))]
print(number_list)
sdvig = int(input("Введите сдвиг: "))
sdvig = sdvig % len(number_list)
print(number_list[-sdvig:] + number_list[:-sdvig])
