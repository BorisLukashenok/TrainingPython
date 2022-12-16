# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint as rnd

stepen = int(input('Введите максимальную степень: '))
lists = list()
stroka = str()
for i in range(stepen,-1,-1):
    multiplier = rnd(0,100)
    if multiplier!=0:
        if i!=0:
            lists+=[f'{multiplier}X^{i}']
        else:
            lists+=[f'{multiplier}']
for i in range(len(lists)):
    if i!=len(lists)-1:
        stroka+=f'{lists[i]} + '
    else:
        stroka+=f'{lists[i]} = 0'

out = open('file_for_task_4.txt','a')
out.writelines(f"{stroka}\n")
out.close()