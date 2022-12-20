num = int(input())
coordinates = [list(map(int, input().split(" "))) for i in range(num)]
dct = {}
for i in range(num):
    tuple = (coordinates[i][0] // 10, coordinates[i][1] // 10)
    if tuple not in dct:
        dct[tuple] = 0
    dct[tuple] += 1
print(max(dct.values()))