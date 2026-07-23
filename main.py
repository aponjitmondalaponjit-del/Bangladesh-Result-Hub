import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📘 SSC Result", "📗 HSC Result"],
        ["🕌 Dakhil Result", "📙 Alim Result"],
        ["👤 My Profile", "📢 Notice"],
        ["💬 Support"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🇧🇩 বাংলাদেশ রেজাল্ট হাব\n\n"
        "স্বাগতম!\n\n"
        "এই বটের মাধ্যমে আপনি বাংলাদেশ শিক্ষা বোর্ডের পরীক্ষার ফলাফল সহজেই দেখতে পারবেন।\n\n"
        "নিচের একটি অপশন নির্বাচন করুন।",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bangladesh Result Hub (BRH) Started...")

    app.run_polling()

if __name__ == "__main__":
    main()
