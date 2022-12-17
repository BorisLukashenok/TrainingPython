# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint as rnd

stepen = int(input('Введите максимальную степень: '))
lists = list()
stroka = str()
for i in range(stepen,-1,-1):
    multiplier = rnd(0,100)
    if multiplier!=0:
        if multiplier==1:
            temp=''
        else:
            temp=str(multiplier)
        if i not in [0,1]:
            lists+=[f'{temp}X^{i}']
        elif i == 1:
            lists+=[f'{temp}X']
        else:
            lists+=[f'{temp}']
for i in range(len(lists)):
    if i!=len(lists)-1:
        stroka+=f'{lists[i]} + '
    else:
        stroka+=f'{lists[i]} = 0'

with open('file_for_task_4.txt','w') as out:
    out.writelines(stroka)
