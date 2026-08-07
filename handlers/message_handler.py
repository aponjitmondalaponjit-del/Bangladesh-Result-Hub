"""
==========================================================
Bangladesh Result Hub (BRH)

Message Handler

Version : 1.0.0

Responsibilities:
- Handle Main Menu buttons
- Open sub menus
==========================================================
"""

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import main_menu
from keyboards.result_menu import result_menu
from keyboards.profile_menu import profile_menu
from keyboards.settings_menu import settings_menu


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Handle Main Menu buttons.
    """

    text = update.message.text or ""
    text = " ".join(text.split())

    print(text)
    
    if text == "📚 Result":
        await update.message.reply_text(
            "📚 একটি পরীক্ষা নির্বাচন করুন।",
            reply_markup=result_menu(),
        )

    elif text == "👤 Profile":
        await update.message.reply_text(
            "👤 Profile Menu",
            reply_markup=profile_menu(),
        )

    elif text == "⚙️ Settings":
        await update.message.reply_text(
            "⚙️ Settings",
            reply_markup=settings_menu(),
        )

    elif text == "🎁 Referral":
        await update.message.reply_text(
            "🎁 Referral System\nComing Soon..."
        )

    elif text == "💎 Premium":
        await update.message.reply_text(
            "💎 Premium System\nComing Soon..."
        )

    elif text == "📢 Notice":
        await update.message.reply_text(
            "কার্যক্রম চলছে"
        )


    elif text == "🆘 Support":
        await update.message.reply_text(
            "🆘 Support\nComing Soon..."
        )

    
    else:
        await update.message.reply_text(
            "অনুগ্রহ করে নিচের মেনু ব্যবহার করুন।",
            reply_markup=main_menu(),
        )
