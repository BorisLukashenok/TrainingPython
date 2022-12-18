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


frend_hand = dict()
for i in frend:
    frend_hand[i] = list()
    for j in frend[i]:
        frend_hand[i] += frend.get(j)  # Добавляем друзей друзей
    frend_hand[i] = list(set(frend_hand[i]))  # Удаляем повторы
    if i in frend_hand[i]:  # Удаляем человека, чей ключ обрабатываем
        frend_hand[i].remove(i)
    for j in frend[i]:  # Удаляем близких друзей
        if j in frend_hand[i]:
            frend_hand[i].remove(j)

for i in sorted(frend_hand):
    print(f"{i}: {', '.join(sorted(frend_hand[i]))}")
