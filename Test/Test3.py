stroka ="-73X^4 + 124X^3 + -76X + -1 = 0"
# Нужно привести к виду - 73X^4 + 124X^3 - 76X - 1 = 0
minus = '-'
if minus in stroka:
    if stroka[0] == minus:
        stroka = '+ '+stroka
    while '+ -' in stroka:  # Виснет на цикле?
        stroka.replace('+ -', '- ')
