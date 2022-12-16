# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# этих двух чисел.

# НОК = (a*b) / НОД(a,b) (алгоритм евклида)
def Nodss( a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

n = int(input())
m = int(input())
a=n
b=m
while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
print(int((n*m)/ a+b))
