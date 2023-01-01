def takeinput(token):
    while True:
        value = input(f'Номер поля, где разместить: {token} ? ')
        if value not in valid or value =='':
            print('Неправильный номер :) ')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print('Поле занято!!!')
            continue
        field[value - 1] = token
        break


def checkwin():
    for each in wins_line:        
        if (field[each[0]]) == (field[each[1]]) == (field[each[2]]):
            return True
    return False