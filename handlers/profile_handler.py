from telegram import Update
from telegram.ext import ContextTypes

from profile import get_profile


async def profile_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        get_profile(
            user.id,
            user.username
        )
    )
