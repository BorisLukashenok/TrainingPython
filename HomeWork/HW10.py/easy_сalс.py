from telegram import Update
import re
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters


def calc(text):
    c = re.sub(r'[^0-9+\.j*/-]+', r'', text)
    try:
        return str(f'Ответ: {eval(c)}')
    except:
        return "Очепятки"


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=calc(update.message.text))

app = ApplicationBuilder().token("5642071095:AAGHwdeHvX3ZaXXg6WKpgEUEMVrE_-IbKqM").build()
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
app.add_handler(echo_handler)
app.run_polling()

