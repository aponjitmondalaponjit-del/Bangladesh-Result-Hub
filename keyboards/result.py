from telegram import ReplyKeyboardMarkup


def result_keyboard():
    keyboard = [
        ["📘 SSC Result"],
        ["📗 HSC Result"],
        ["🕌 Dakhil Result"],
        ["📙 Alim Result"],
        ["⬅️ Back"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
