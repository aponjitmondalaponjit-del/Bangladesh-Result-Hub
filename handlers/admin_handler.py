from telegram import Update
from telegram.ext import ContextTypes

from admin import get_admin_panel


async def admin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        get_admin_panel()
    )
