"""
==========================================================
Bangladesh Result Hub (BRH)

Start Handler

Version : 1.0.0

Responsibilities:
- Handle /start command
- Show Main Menu
==========================================================
"""

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import main_menu


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Handle /start command.
    """

    await update.message.reply_text(
        text="🇧🇩 বাংলাদেশ রেজাল্ট হাবে স্বাগতম",
        reply_markup=main_menu(),
    )
