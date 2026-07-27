from telegram import ReplyKeyboardMarkup


def support_keyboard():
    keyboard = [
        ["❓ Frequently Asked Questions"],
        ["📝 Create Support Ticket"],
        ["📂 My Tickets"],
        ["⬅️ Back", "🏠 Home"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
