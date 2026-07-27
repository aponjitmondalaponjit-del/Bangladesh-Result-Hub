from telegram import ReplyKeyboardMarkup


def profile_keyboard():
    keyboard = [
        ["✏️ Edit Profile"],
        ["🔔 Result Notification"],
        ["🌐 Change Language"],
        ["⬅️ Back", "🏠 Home"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
