# 2. Задайте список. Напишите программу, которая определит, присутствует ли в списке строк некое число.

arr = ['asds', 'ffrfr34dffdvdf', 'dfvfd2424vfv']
n = '354'
flag = False
for i in arr:
    if n in i:
        flag = True
        print('yes')

if not flag:
    print('no')
