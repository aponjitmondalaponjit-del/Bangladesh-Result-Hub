from telegram.ext import Application

from config import BOT_TOKEN
from handlers.handler_registration import register_handlers


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    register_handlers(app)

    print("🇧🇩 Bangladesh Result Hub Bot Started")

    try:
        app.run_polling()
    except Exception as e:
        print(f"BOT ERROR: {e}")
        raise


if __name__ == "__main__":
    main()
