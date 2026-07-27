from referral import get_user


def get_profile(user_id, username):
    user = get_user(user_id)

    if not user:
        return "❌ User not found."

    profile_status = "🔓 Unlocked" if user["referrals"] >= 3 else "🔒 Locked"

    premium_status = (
        "🏆 Free Premium"
        if user["referrals"] >= 150
        else "💳 Paid Required"
    )

    return (
        "👤 Bangladesh Result Hub Profile\n\n"
        f"🆔 User ID: {user_id}\n"
        f"👤 Username: @{username if username else 'None'}\n\n"
        f"👥 Total Referrals: {user['referrals']}\n"
        f"📂 Profile Status: {profile_status}\n"
        f"💎 Premium Status: {premium_status}\n\n"
        "━━━━━━━━━━━━━━\n"
        "✅ ৩টি রেফার সম্পন্ন হলে Profile Unlock হবে।\n"
        "🏆 ১৫০টি রেফার সম্পন্ন হলে সকল Premium Feature বিনামূল্যে ব্যবহার করতে পারবেন।"
    )
