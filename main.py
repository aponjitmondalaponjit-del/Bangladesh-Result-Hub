"""
==========================================================
Bangladesh Result Hub (BRH)

Main Application

Version : 1.0.0

Responsibilities:
- Start Telegram Bot
- Load configuration
- Register handlers
- Set Telegram Menu Button
==========================================================
"""

from telegram.ext import Application

from config import BOT_TOKEN
from handlers.handler_registration import register_handlers
from handlers.post_init import post_init


def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    register_handlers(app)

    print("🇧🇩 Bangladesh Result Hub Bot Started")

    try:
        app.run_polling()
    except Exception as e:
        print(f"BOT ERROR: {e}")
        raise


if __name__ == "__main__":
    main()
