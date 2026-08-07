from telegram import Update
from telegram.ext import ContextTypes


async def support_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Support\nখুব শীগ্রই চালু হবে.."
    )
