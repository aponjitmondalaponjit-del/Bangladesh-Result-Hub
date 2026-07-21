import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇧🇩 Bangladesh Result Hub (BRH)\n\n"
        "Welcome!\n"
        "The bot is currently under development."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bangladesh Result Hub (BRH) Started...")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
