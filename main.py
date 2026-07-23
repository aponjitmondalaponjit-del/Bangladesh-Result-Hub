import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📘 SSC Result", "📗 HSC Result"],
        ["🕌 Dakhil Result", "📙 Alim Result"],
        ["👤 My Profile", "📢 Notice"],
        ["💬 Support"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "🇧🇩 বাংলাদেশ রেজাল্ট হাব\n\n"
        "স্বাগতম!\n\n"
        "এই বটের মাধ্যমে আপনি বাংলাদেশ শিক্ষা বোর্ডের পরীক্ষার ফলাফল সহজেই দেখতে পারবেন।\n\n"
        "নিচের একটি অপশন নির্বাচন করুন।",
        reply_markup=reply_markup,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📘 SSC Result":
        await update.message.reply_text(
            "📘 SSC Result\n\n"
            "এই ফিচারটি শীঘ্রই চালু হবে।"
        )

    elif text == "📗 HSC Result":
        await update.message.reply_text(
            "📗 HSC Result\n\n"
            "এই ফিচারটি শীঘ্রই চালু হবে।"
        )

    elif text == "🕌 Dakhil Result":
        await update.message.reply_text(
            "🕌 Dakhil Result\n\n"
            "এই ফিচারটি শীঘ্রই চালু হবে।"
        )

    elif text == "📙 Alim Result":
        await update.message.reply_text(
            "📙 Alim Result\n\n"
            "এই ফিচারটি শীঘ্রই চালু হবে।"
        )

    elif text == "👤 My Profile":
        await update.message.reply_text(
            "👤 My Profile\n\n"
            "প্রোফাইল সিস্টেম শীঘ্রই যুক্ত করা হবে।"
        )

    elif text == "📢 Notice":
        await update.message.reply_text(
            "📢 Notice\n\n"
            "বর্তমানে কোনো নতুন নোটিশ নেই।"
        )

    elif text == "💬 Support":
        await update.message.reply_text(
            "💬 Support\n\n"
            "সহায়তা সিস্টেম শীঘ্রই যুক্ত করা হবে।"
        )

    else:
        await update.message.reply_text(
            "অনুগ্রহ করে নিচের মেনু থেকে একটি অপশন নির্বাচন করুন।"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("Bangladesh Result Hub (BRH) Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
