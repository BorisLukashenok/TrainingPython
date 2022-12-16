# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Задайте число: "))
multipliers = []
divider = 2
while divider * divider <= n:
    if n % divider == 0:
        multipliers.append(divider)
        n //= divider
    else:
        divider += 1
if n > 1:
    multipliers.append(n)

print(f"Простые множители: {multipliers}")
