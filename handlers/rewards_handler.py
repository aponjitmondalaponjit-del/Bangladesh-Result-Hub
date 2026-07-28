from telegram import Update
from telegram.ext import ContextTypes

from rewards import get_rewards


async def rewards_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        get_rewards(user.id)
    )
