from telegram import KeyboardButton, ReplyKeyboardMarkup


def settings_menu():
    keyboard = [
        [KeyboardButton("🌐 Language")],
        [KeyboardButton("🔔 Notification")],
        [KeyboardButton("🔙 Main Menu")],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )
