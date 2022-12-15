# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число: '))

bites = ""

while number > 0:
    bites = str(number % 2) + bites
    number = number // 2

print(f'Двоичное: {bites}')
