print ("BRH VERSION 2")

import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("8710826860:AAG3gALXky9qAUdxF2PWaUtwKEgzwJgZe1U")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 View Result"],
        ["👤 My Profile", "👥 My Referrals"],
        ["🎁 My Rewards", "📢 Notice"],
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
        "👇 নিচের একটি অপশন নির্বাচন করুন।",
        reply_markup=reply_markup,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📄 View Result":
        await update.message.reply_text(
            "📄 View Result\n\n"
            "নিচের একটি পরীক্ষা নির্বাচন করুন।\n\n"
            "📘 SSC Result\n"
            "📗 HSC Result\n"
            "🕌 Dakhil Result\n"
            "📙 Alim Result\n\n"
            "🚧 এই অংশের বাটনগুলো আমরা পরবর্তী ধাপে যোগ করব।"
        )

    elif text == "👤 My Profile":
        await update.message.reply_text(
            "👤 My Profile\n\n"
            "🔒 আপনি এখনও ৩টি রেফার সম্পন্ন করেননি।\n\n"
            "৩টি রেফার সম্পন্ন হলে প্রোফাইল আনলক হবে।"
        )

    elif text == "👥 My Referrals":
        await update.message.reply_text(
            "👥 My Referrals\n\n"
            "আপনার মোট রেফার: ০\n\n"
            "🔗 আপনার ইউনিক রেফারেল লিংক পরে এখানে দেখানো হবে।"
        )

    elif text == "🎁 My Rewards":
        await update.message.reply_text(
            "🎁 My Rewards\n\n"
            "এখনও কোনো রিওয়ার্ড পাওয়া যায়নি।"
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
