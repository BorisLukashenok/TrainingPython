def print_dikt(slovar):
    for i in slovar:
        if slovar[i] != None:
            print(f"{i}: {slovar[i]}")


def rev(n):
    if n == 0:
        n = 1
    else:
        n = 0
    return n


dicts = dict()
lists = list()
flag = True
while flag:
    stroka = input()
    if stroka != "":
        lists = stroka.split(" ")
        for i in range(2):
            if lists[i] not in dicts:
                dicts[lists[i]] = [lists[rev(i)]]
            else:
                dicts[lists[i]] += [lists[rev(i)]]
    else:
        flag = not flag

print("Друзья первого рукопожатия")
print_dikt(dicts)
dicts2 = {}
for i in dicts:
    dicts2[i] = list()
    for j in dicts[i]:
        dicts2[i] += dicts.get(j)  # добавляем друзей друзей
        while i in dicts2[i]:  # удаляем текушую фамилию
            dicts2[i].remove(i)
    dicts2[i] = list(set(dicts2[i]))  # удаляем повторы
print("Друзья второго рукопожатия")
print_dikt(dicts2)
