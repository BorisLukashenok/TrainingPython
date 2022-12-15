# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит,
#  что её нет.

arr = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
n = "qwe"
count = 0
for i in range(len(arr)):
    if arr[i] == n:
        count += 1
    if count == 2:
        print(i)
if count == 0:
    print("Нет")
