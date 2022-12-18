# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
file_1 = "file_for_task_5_1.txt"
file_2 = "file_for_task_5_2.txt"
file_out = "file_for_task_5_out.txt"


def prepare(file_name):
    with open(file_name, "r") as inp:
        polyn = inp.read()
    pol_dk = dict()
    polyn = polyn.replace(" = 0", "")
    pol_ls = polyn.split(" + ")
    for i in range(len(pol_ls)):
        if "X" in pol_ls[i]:
            stroka = pol_ls[i][: pol_ls[i].find("X")]
            if "^" in pol_ls[i]:
                key = int(pol_ls[i][pol_ls[i].find("^") + 1 :])
            else:
                key = 1
            pol_dk[key] = 1 if stroka == "" else int(stroka)
        else:
            pol_dk[0] = int(pol_ls[i])

    return pol_dk


polynom_1 = prepare(file_1)
polynom_2 = prepare(file_2)
polynom_sum = dict()
stepen = max(max(i for i in polynom_1), max(i for i in polynom_2))
for i in range(stepen + 1):
    if polynom_1.get(i) == None:
        polynom_1[i] = 0
    if polynom_2.get(i) == None:
        polynom_2[i] = 0
    polynom_sum[i] = polynom_1[i] + polynom_2[i]
lists = list()
for i in range(stepen, -1, -1):
    multiplier = polynom_sum[i]
    if multiplier != 0:
        if multiplier == 1:
            if i == 0:
                temp = "1"
            else:
                temp = ""
        else:
            temp = str(multiplier)
        if i not in [0, 1]:
            lists += [f"{temp}X^{i}"]
        elif i == 1:
            lists += [f"{temp}X"]
        else:
            lists += [f"{temp}"]
stroka = f"{' + '.join(lists)} = 0"

print(stroka)
with open(file_out, "w") as out:
    out.writelines(stroka)
