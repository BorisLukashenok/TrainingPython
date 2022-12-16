def print_dikt(slovar):
    for i in slovar:
        if slovar[i] != None:
            print(f"{i}: {slovar[i]}")


dicts = dict()
lists = list()
while True:
    stroka = input()
    if stroka != "":
        lists = stroka.split(" ")
        if lists[0] not in dicts:
            dicts[lists[0]] = [lists[1]]
        else:
            dicts[lists[0]] += [lists[1]]
        if lists[1] not in dicts:
            dicts[lists[1]] = [lists[0]]
        else:
            dicts[lists[1]] += [lists[0]]
    elif stroka == "":
        break
print('Друзья первого рукопожатия')
print_dikt(dicts)
dicts2 = {}
lists = list()
for i in dicts:
    for j in dicts[i]:
        lists += list(dicts.get(j))
        while i in lists:
            lists.remove(i)
    lists = list(set(lists))
    dicts2[i] = lists
    lists = list()
print('Друзья второго рукопожатия')
print_dikt(dicts2)
