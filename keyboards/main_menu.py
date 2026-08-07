from telegram import KeyboardButton, ReplyKeyboardMarkup


def main_menu():
    keyboard = [
        [
            KeyboardButton("📚 Result"),
            KeyboardButton("👤 Profile"),
        ],
        [
            KeyboardButton("🎁 Referral"),
            KeyboardButton("📢 Notice"),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )
