from telegram import ReplyKeyboardMarkup


def admin_keyboard():
    keyboard = [
        ["📢 Notice Management", "🎫 Support Tickets"],
        ["👥 User Management", "🏆 Leaderboard"],
        ["⚙️ System Settings"],
        ["⬅️ Back", "🏠 Home"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
