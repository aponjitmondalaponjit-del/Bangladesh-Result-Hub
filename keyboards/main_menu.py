from telegram import ReplyKeyboardMarkup


def main_menu():
    keyboard = [
        ["📚 Result", "👤 Profile"],
        ["🎁 Referral", "💎 Premium"],
        ["⚙️ Settings", "📢 Notice"],
        ["🛒 Products", "🆘 Support"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
