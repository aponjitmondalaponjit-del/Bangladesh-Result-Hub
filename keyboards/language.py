from telegram import ReplyKeyboardMarkup


def language_keyboard():
    keyboard = [
        ["🇧🇩 বাংলা", "🇬🇧 English"],
        ["🇮🇳 हिन्दी", "🇸🇦 العربية"],
        ["⬅️ Back"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
