from telegram import Update
from telegram.ext import ContextTypes

from keyboards.home import home_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🇧🇩 *Bangladesh Result Hub (BRH)*\n\n"
        "স্বাগতম!\n\n"
        "এই বটের মাধ্যমে আপনি বাংলাদেশ শিক্ষা বোর্ডের পরীক্ষার ফলাফল সহজেই দেখতে পারবেন।\n\n"
        "👇 নিচের একটি অপশন নির্বাচন করুন।"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=home_keyboard(),
        parse_mode="Markdown"
    )
