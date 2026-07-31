from telegram import Update
from telegram.ext import ContextTypes

from keyboards.result_menu import result_menu


async def result_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "📚 একটি পরীক্ষা নির্বাচন করুন।",
        reply_markup=result_menu(),
    )
