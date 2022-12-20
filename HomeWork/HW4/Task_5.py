# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
file_1 = "file_for_task_5_1.txt"
file_2 = "file_for_task_5_2.txt"
file_out = "file_for_task_5_out.txt"
minus = '-'


def prepare(file_name):
    with open(file_name, "r") as inp:
        pol_ls = inp.read().replace(" = 0\n", "").split()
    if len(pol_ls) % 2 != 0:
        pol_ls.insert(0, '+')
    print(pol_ls)
    pol_dk = dict()
    for i in range(1, len(pol_ls), 2):
        if "X" in pol_ls[i]:
            stroka = pol_ls[i][: pol_ls[i].find("X")]
            if "^" in pol_ls[i]:
                key = int(pol_ls[i][pol_ls[i].find("^") + 1:])
            else:
                key = 1
            pol_dk[key] = 1 if stroka == "" else int(stroka)
        else:
            key = 0
            pol_dk[key] = int(pol_ls[i])
        if pol_ls[i-1] == minus:
            pol_dk[key] = - pol_dk[key]            
    return pol_dk


polynom_1 = prepare(file_1)
polynom_2 = prepare(file_2)
polynom_sum = dict()
stepen = max(max(i for i in polynom_1), max(i for i in polynom_2))
for i in range(stepen + 1):
    polynom_sum[i] = (polynom_1[i] if polynom_1.get(i) != None else 0) + (
        polynom_2[i] if polynom_2.get(i) != None else 0)
lists = list()
for i in range(stepen, -1, -1):
    if polynom_sum[i] != 0:
        if polynom_sum[i] == 1:
            if i == 0:
                temp = "1"
            else:
                temp = ""
        else:
            temp = str(polynom_sum[i])
        if i not in [0, 1]:
            lists += [f"{temp}X^{i}"]
        elif i == 1:
            lists += [f"{temp}X"]
        else:
            lists += [f"{temp}"]
stroka = f"{' + '.join(lists)} = 0"
if minus in stroka:
    if stroka[0] == minus:
        stroka = '+ ' + stroka
    stroka = stroka.replace('+ -', '- ')
print(stroka)
with open(file_out, "w") as out:
    out.writelines(stroka)
