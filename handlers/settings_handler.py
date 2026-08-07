from telegram import Update
from telegram.ext import ContextTypes

from keyboards.settings_menu import settings_menu


async def settings_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚙️ Settings",
        reply_markup=settings_menu(),
    )
