file_bok_str = 'Book1.txt'
file_bok_list = 'Book2.txt'


def readfile_str(file_bok):
    with open(file_bok, "r", encoding="utf_8") as s:
        return s.read().replace('\n', ', ').split(', ')


def readfile_list(file_bok):
    with open(file_bok, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ''), s.readlines()))


def scan():
    # Просмотр всех записей справочника:
    data1 = readfile_list(file_bok_str)
    data2 = readfile_list(file_bok_list)
    for i, v in enumerate(data1, 1):
        print(f"{i}. {v}")
    for i, v in enumerate(data2, 1):
        print(f"{i}. {v}")


# def search(data):
#     # Поиск по справочнику.
#     flag = 1
#     name = input('имя > ')
#     for line in data:
#         if name in line:
#             flag = 0
#             print(line)
#     if flag: print('no name given')


def add_contact_str():
    with open(file_bok_str, "a", encoding="utf_8") as data:
        data.write(", ".join(input().title().split())+"\n")


def add_contact_list():
    with open(file_bok_list, "a", encoding="utf_8") as data:
        data.write(str("\n".join(input().title().split())+'\n\n'))


# При запуске программы (скрипта), она должна считывать содержимое

# # # словарь команд, в значениях функции их исполняющие
dict_command = {'1':  scan, '2': add_contact_str}

print('''Команды для работы со справочником:
    Просмотр всех записей справочника:  - 1
    Поиск по справочнику -2
    Добавление новой записи - 3
     Удаление записи из справочника по Имени и Фамилии - 4
     Изменение любого поля в определенной записи справочника - 5 
     Вывод возраста человека (записи) по Имени и Фамилии - 6 ''')

while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command]()
    else:
        print(' command error!')

# print(readfile_list(file_bok_list))
# print(readfile_str(file_bok_str))
