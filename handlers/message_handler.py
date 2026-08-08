"""
==========================================================
Bangladesh Result Hub (BRH)

Message Handler

Version : 1.0.0

Responsibilities:
- Handle Main Menu buttons only
- Open Result menu
- Open Profile
- Open Referral
- Open Notice
- Return to Main Menu

Main Menu:
📚 Result
👤 Profile
🎁 Referral
📢 Notice

Side Menu is handled separately through commands:
💎 Premium
⚙️ Settings
🆘 Support
==========================================================
"""

from telegram import Update
from telegram.ext import ContextTypes

from keyboards.main_menu import main_menu
from keyboards.result_menu import result_menu


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Handle Main Menu buttons only.
    """

    # ==========================================================
    # Safety Check
    # ==========================================================

    if not update.message:
        return

    text = update.message.text or ""
    text = " ".join(text.split())

    print(f"📩 User selected: {text}")

    # ==========================================================
    # 📚 Result
    # ==========================================================

    if text == "📚 Result":

        # ------------------------------------------------------
        # IMPORTANT:
        # Future flow for General/Free User:
        #
        # 1. User selects Result
        # 2. 10-second advertisement
        # 3. Advertisement completed
        # 4. Result Menu opens
        #
        # Premium User:
        # Direct access without advertisement
        #
        # The actual advertisement system will be connected
        # later. Do NOT show Result Menu immediately as an
        # advertisement has not been implemented yet.
        # ------------------------------------------------------

        await update.message.reply_text(
            "📺 রেজাল্ট দেখতে হলে আগে ১০ সেকেন্ডের বিজ্ঞাপন দেখতে হবে।\n\n"
            "বিজ্ঞাপন ব্যবস্থা শীঘ্রই যুক্ত করা হবে।"
        )

    # ==========================================================
    # 👤 Profile
    # ==========================================================

    elif text == "👤 Profile":

        await update.message.reply_text(
            "👤 Profile\n\n"
            "Profile System শীঘ্রই চালু হবে।"
        )

    # ==========================================================
    # 🎁 Referral
    # ==========================================================

    elif text == "🎁 Referral":

        await update.message.reply_text(
            "🎁 Referral\n\n"
            "Referral System শীঘ্রই চালু হবে।"
        )

    # ==========================================================
    # 📢 Notice
    # ==========================================================

    elif text == "📢 Notice":

        await update.message.reply_text(
            "📢 Notice\n\n"
            "বর্তমানে কোনো নতুন Notice নেই।"
        )

    # ==========================================================
    # 🔙 Main Menu
    # ==========================================================

    elif text in (
        "🔙 Main Menu",
        "⬅️ Main Menu",
        "↩️ Main Menu",
    ):

        await update.message.reply_text(
            "🇧🇩 Bangladesh Result Hub (BRH)",
            reply_markup=main_menu(),
        )

    # ==========================================================
    # Unknown Text
    # ==========================================================

    else:

        await update.message.reply_text(
            "অনুগ্রহ করে নিচের Main Menu ব্যবহার করুন।",
            reply_markup=main_menu(),
        )
