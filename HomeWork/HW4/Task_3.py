# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

print(*set(map(int, input("Введите числа через пробел: ").split(" "))))
