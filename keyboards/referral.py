from telegram import ReplyKeyboardMarkup


def referral_keyboard():
    keyboard = [
        ["🔗 My Referral Link"],
        ["🏆 Leaderboard"],
        ["📜 Referral Rules"],
        ["⬅️ Back", "🏠 Home"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
