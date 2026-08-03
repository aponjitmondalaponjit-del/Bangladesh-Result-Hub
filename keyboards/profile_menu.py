"""
==========================================================
Bangladesh Result Hub (BRH)

Profile Menu Keyboard

Version : 1.0.0

Responsibilities:
- Show Profile Menu
==========================================================
"""

from telegram import ReplyKeyboardMarkup


def profile_menu():
    """
    Profile Menu Keyboard
    """

    keyboard = [
        ["👤 আমার প্রোফাইল"],
        ["📄 Save My Roll"],
        ["👥 Referral"],
        ["🎁 Rewards"],
        ["💎 Premium"],
        ["🔙 Main Menu"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )
