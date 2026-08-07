from telegram import ReplyKeyboardMarkup


def main_menu():
    keyboard = [
        ["📚 Result", "👤 Profile"],
        ["🎁 Referral", "📢 Notice"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True,
    )
