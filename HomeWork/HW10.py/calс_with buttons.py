import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

value = ''
old_value = ''

keyboard = [
    [
        InlineKeyboardButton(" ", callback_data="no"),
        InlineKeyboardButton("C", callback_data="C"),
        InlineKeyboardButton("<=", callback_data="<="),
        InlineKeyboardButton("/", callback_data="/"),
    ],
    [
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("*", callback_data="*"),
    ],
    [
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("-", callback_data="-"),
    ],
    [
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("+", callback_data="+"),
    ],
    [
        InlineKeyboardButton(" ", callback_data="no"),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton(",", callback_data="."),
        InlineKeyboardButton("=", callback_data="="),
    ]
]


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    global value
    if value == "":
        await update.message.reply_text(text="0", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.message.reply_text(text=value, reply_markup=InlineKeyboardMarkup(keyboard))

value = ''
old_value = ''


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value, old_value
    data = update.callback_query
    await data.answer()

    if data[0] == "C":
        value = ""
    elif data[0] == "=":
        try:
            value = str(eval(value))
        except:
            value = "Ошибка!"
    else:
        value += str(data[0])

    if value != old_value:
        if value == "":
            await data.edit_message_text(text="0", reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            await data.edit_message_text(text=value, reply_markup=InlineKeyboardMarkup(keyboard))

    old_value = value
    if value == "Ошибка!":
        value = ""

    # await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the bot and pass it your bot's token.
    bot = Application.builder().token(
        "5642071095:AAGHwdeHvX3ZaXXg6WKpgEUEMVrE_-IbKqM").build()

    bot.add_handler(CommandHandler("calc", calc))
    bot.add_handler(CallbackQueryHandler(button))
    bot.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    bot.run_polling()


if __name__ == "__main__":
    main()
