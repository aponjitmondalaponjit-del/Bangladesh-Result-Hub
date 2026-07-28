from telegram import Update
from telegram.ext import ContextTypes

from profile import get_profile
from keyboards.result import result_keyboard
from keyboards.settings import settings_keyboard
from keyboards.language import language_keyboard
from keyboards.referral import referral_keyboard
from keyboards.support import support_keyboard


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    if text == "📄 View Result":
        await update.message.reply_text(
            "📄 Select an Exam",
            reply_markup=result_keyboard()
        )

    elif text == "👤 My Profile":
        await update.message.reply_text(
            get_profile(user.id, user.username)
        )

    elif text == "👥 My Referrals":
        await update.message.reply_text(
            "👥 Referral Menu",
            reply_markup=referral_keyboard()
        )

    elif text == "⚙️ Settings":
        await update.message.reply_text(
            "⚙️ Settings",
            reply_markup=settings_keyboard()
        )

    elif text == "🌐 Language":
        await update.message.reply_text(
            "🌐 Select Language",
            reply_markup=language_keyboard()
        )

    elif text == "💬 Support":
        await update.message.reply_text(
            "💬 Support Center",
            reply_markup=support_keyboard()
        )

    else:
        await update.message.reply_text(
            "❌ Unknown option."
        )
