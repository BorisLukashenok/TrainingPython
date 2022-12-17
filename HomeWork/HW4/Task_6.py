def print_dikt(slovar):
    for i in slovar:
        if slovar[i] != None:
            print(f"{i}: {slovar[i]}")


def rev(n):
    return 1 if n == 0 else 0


frend = dict()
lists = list()
flag = True
while flag:
    lists = input().split(" ")
    if len(lists) != 1:
        for i in range(2):
            if lists[i] not in frend:
                frend[lists[i]] = [lists[rev(i)]]
            else:
                frend[lists[i]] += [lists[rev(i)]]
    else:
        flag = not flag

print("Друзья первого рукопожатия")
print_dikt(frend)
frend_hand = {}
for i in frend:
    frend_hand[i] = list()
    for j in frend[i]:
        frend_hand[i] += frend.get(j)  # добавляем друзей друзей
    frend_hand[i] = list(set(frend_hand[i]))  # удаляем повторы
    while i in frend_hand[i]:  # удаляем текущую фамилию
        frend_hand[i].remove(i)

print("Друзья второго рукопожатия")
print_dikt(frend_hand)
