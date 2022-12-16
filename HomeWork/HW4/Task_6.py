def print_dikt(slovar):
    for i in slovar:
        if slovar[i] != None:
            print(f"{i}: {slovar[i]}")


def rev(n):
    return 1 if n == 0 else 0


dicts = dict()
lists = list()
flag = True
while flag:
    lists = input().split(" ")
    if len(lists) != 1:
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
