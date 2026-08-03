"""
==========================================================
Bangladesh Result Hub (BRH)

Settings Menu Keyboard

Version : 1.0.0

Responsibilities:
- Show Settings Menu
==========================================================
"""

from telegram import ReplyKeyboardMarkup


def settings_menu():
    """
    Settings Menu Keyboard
    """

    keyboard = [
        ["🌐 Language"],
        ["🔔 Notification"],
        ["📢 Ads Settings"],
        ["ℹ️ Notice"],
        ["🔙 Main Menu"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )
