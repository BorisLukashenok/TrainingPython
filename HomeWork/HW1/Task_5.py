# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

print('Введите координаты 1ой точки: ')
x1 = int(input('X = '))
y1 = int(input('Y = '))
print('Введите координаты 2ой точки: ')
x2 = int(input('X = '))
y2 = int(input('Y = '))
print(f'Расстояние между точками = {round(((( x2- x1)**2 + (y2 - y1)**2)**0.5),2)}')