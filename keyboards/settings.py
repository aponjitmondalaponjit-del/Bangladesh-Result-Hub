from telegram import ReplyKeyboardMarkup


def settings_keyboard():
    keyboard = [
        ["👤 Edit Profile"],
        ["🔔 Result Notification"],
        ["🌐 Change Language"],
        ["⬅️ Back"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
