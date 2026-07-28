from telegram import Update
from telegram.ext import ContextTypes

from support import get_support_message


async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        get_support_message()
    )
