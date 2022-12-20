a = input().split()
for i in a:
    if 'абв' in i.lower():
        a.remove(i)
print(f'{" ".join(a)}')

