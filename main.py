from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇧🇩 Welcome to Bangladesh Result Hub (BRH)\n\n"
        "Bot is under development.\n"
        "Thank you for testing ❤️"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("BRH Bot Started...")

    app.run_polling()

if __name__ == "__main__":
    main()
