from telegram import ReplyKeyboardMarkup


def home_keyboard():
    keyboard = [
        ["📄 View Result"],
        ["👤 My Profile", "👥 My Referrals"],
        ["🎁 My Rewards", "📢 Notice"],
        ["💬 Support"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        persistent=True
    )
