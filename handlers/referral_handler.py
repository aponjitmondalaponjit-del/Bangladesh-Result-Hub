from telegram import Update
from telegram.ext import ContextTypes

from referral import get_referral_text


async def referral_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        get_referral_text(user.id)
    )
