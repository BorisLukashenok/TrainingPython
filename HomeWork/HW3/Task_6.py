number = int(input("Введите число: "))
negafib3 = lambda n: n if n < 2  else negafib3(n - 1) + negafib3(n - 2)
negafib4 = lambda n: negafib3(n) if n >= 0 else round(negafib4(abs(n)) * (-1)**(n + 1))
print([negafib4(num) for num in range(-number, number + 1)])
