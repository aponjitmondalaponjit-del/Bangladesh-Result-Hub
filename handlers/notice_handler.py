from telegram import Update
from telegram.ext import ContextTypes

from notice import get_notice


async def notice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        get_notice()
    )
