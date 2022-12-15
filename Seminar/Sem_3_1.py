# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных 
# чисел.
# random.seed(число)        time, datetime, psutil

from time import time
print(str(time())[-3:])
