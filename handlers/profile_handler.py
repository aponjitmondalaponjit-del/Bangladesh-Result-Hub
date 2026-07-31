from telegram import Update
from telegram.ext import ContextTypes

from keyboards.profile_menu import profile_menu


async def profile_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "👤 Profile Menu",
        reply_markup=profile_menu(),
    )
