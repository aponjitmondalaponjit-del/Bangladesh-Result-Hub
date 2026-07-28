from telegram import Update
from telegram.ext import ContextTypes

from result import get_result_menu


async def result_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        get_result_menu()
    )
