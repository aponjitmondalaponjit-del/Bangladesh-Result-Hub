from telegram import Update
from telegram.ext import ContextTypes

from referral import register_user
from keyboards.home import home_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    register_user(user.id, user.username)

    await update.message.reply_text(
        "🇧🇩 বাংলাদেশ রেজাল্ট হাব (BRH)\n\n"
        "স্বাগতম!\n\n"
        "বাংলাদেশ শিক্ষা বোর্ডের সকল পরীক্ষার ফলাফল, "
        "নোটিশ, রেফারেল এবং আরও অনেক সুবিধা এখানে পাবেন।",
        reply_markup=home_keyboard()
    )
