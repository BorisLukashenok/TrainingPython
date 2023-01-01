from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)



from random import randint as rnd
field_p = list(' ' for i in range(1, 10))
valid = list(map(str, range(0,10)))
print(valid)
wins_line = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
token =' '

async def draw_field(update: Update, context: ContextTypes.DEFAULT_TYPE):
    field = [
        [
            InlineKeyboardButton(token, callback_data='0'),
            InlineKeyboardButton(token, callback_data='1'),
            InlineKeyboardButton(token, callback_data='2'),
        ],
         [
            InlineKeyboardButton(token, callback_data="3"),
            InlineKeyboardButton(token, callback_data="4"),
            InlineKeyboardButton(token, callback_data="5"),
        ],
        [
            InlineKeyboardButton(token, callback_data="5"),
            InlineKeyboardButton(token, callback_data="7"),
            InlineKeyboardButton(token, callback_data="8"),
        ],
    ]
    await update.message.reply_text(text="0", reply_markup=InlineKeyboardMarkup(field))
    return 

count = 0
simbols = ('X', 'O') if rnd(0, 100) % 2 else ('O', 'X')
flag = True
while flag:
    draw_field()   
    takeinput(simbols[count % 2])
    if checkwin():
        draw_field()
        print(simbols[count % 2], 'Ты победил!!!')
        flag = not flag
    else:
        count += 1
        if count > 8:
            draw_field()
            print('Ничья!')
            flag = not flag
