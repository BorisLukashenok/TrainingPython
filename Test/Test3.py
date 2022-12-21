from sys import getsizeof

# Создаём итератор из одного миллиона целых чисел
numbers_iter = (i for i in range(10 ** 6))
# Выводим количество байт, занятых итератором
print(f"Итератор занимает {getsizeof(numbers_iter)} байт.")
# Создаём список
numbers_list = list(range(10 ** 6))
# Выводим количество байт, занятых списком
print(f"Список занимает {getsizeof(numbers_list)} байт.")
