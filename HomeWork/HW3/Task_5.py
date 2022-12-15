num_fib = {-1: 1, 0: 0, 1: 1}
number = int(input('Введите число: '))
def fib(n):
    if n in num_fib:
        return num_fib[n]
    if n < 0:    
        num_fib[n] = fib(n + 2) - fib(n + 1) 
    else:
        num_fib[n] = fib(n - 1) + fib(n - 2)
    return num_fib[n]
for i in range(-number,number + 1):
    print(f'Позиция: {i:3} => {fib(i)}')