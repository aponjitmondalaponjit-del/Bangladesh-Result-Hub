"""
==========================================================
Bangladesh Result Hub (BRH)

Result Menu Keyboard

Version : 1.0.0

Responsibilities:
- Show Result Menu
==========================================================
"""

from telegram import ReplyKeyboardMarkup


def result_menu():
    """
    Result Menu Keyboard
    """

    keyboard = [
        ["📚 SSC", "🎓 HSC"],
        ["🕌 Dakhil", "📖 Alim"],
        ["🏫 Technical"],
        ["🔙 Main Menu"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )
