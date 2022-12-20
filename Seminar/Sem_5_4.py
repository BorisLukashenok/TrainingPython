from random import randint as rnd
board = list(range(1, 10))
wins_line = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
              (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|',
              board[2 + i * 3], "|")
    print('-------------')
    print()


def takeinput(player_token):
    while True:
        value = input(f'Где разместить: {player_token} ? ')
        if value not in '123456789' or value == '':
            print('Неправильный номер :) ')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Поле занято.')
            continue
        board[value - 1] = player_token
        break


def checkwin():
    for each in wins_line:
        print(board[each[0]],board[each[1]],board[each[2]])
        if (board[each[0]]) == (board[each[1]]) == (board[each[2]]):
            return board[each[1]]
    return ''


counter = 0
simbol =('X','O') if rnd(0,2) == 0 else ('O','X')
flag = True
while flag:
    draw_board()    
    print(simbol)
    if counter % 2 == 0:
        takeinput(simbol[0])
    else:
        takeinput(simbol[1])
    if counter > 3:
        winner = checkwin()
        if winner != '':
            draw_board()
            print(winner, 'Ты победил!!!')
            flag = not flag
            continue
    counter += 1
    if counter > 8:
        draw_board()
        print('Ничья!')
        flag = not flag
