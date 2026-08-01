"""
==========================================================
Bangladesh Result Hub (BRH)

Main Application

Version : 1.0.0

Responsibilities:
- Start Telegram Bot
- Load configuration
- Register handlers
- Run polling
==========================================================
"""

from telegram.ext import Application

from config import BOT_TOKEN
from handlers.handler_registration import register_handlers


def main() -> None:
    """
    Start BRH Bot.
    """

    app = Application.builder().token(
        BOT_TOKEN
    ).build()

    register_handlers(app)

    print("🇧🇩 Bangladesh Result Hub Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
