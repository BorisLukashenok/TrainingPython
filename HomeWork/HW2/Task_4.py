import random
DI = 40
num_stud = int(input('Число учеников: '))
class_by_height = [random.randint(int(190 - DI / num_stud * (i+1)), int(190 - DI / num_stud * i)) for i in range(num_stud)]
print(class_by_height)
rostP = int(input('Рост Пети: '))
for i in range(num_stud):
    if rostP >= class_by_height[i]:
        print(f'Место Пети {i+1}е слева')
        break