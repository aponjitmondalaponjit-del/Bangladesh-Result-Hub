from telegram import Update
from telegram.ext import ContextTypes

from keyboards.language import language_keyboard


async def language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Select Your Language",
        reply_markup=language_keyboard()
    )
