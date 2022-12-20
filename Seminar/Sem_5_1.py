def searh_num(arr):
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i-1]:
            return i + 1
    return ' ok'

with open('1.txt', 'r') as f:
    # arr = [int(i) for i in f.read().split()] 
    arr = list(map(int, f.read().split()))

print(searh_num(arr))


