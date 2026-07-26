from referral import get_user

def get_profile(user):
    data = get_user(user.id)

    return (
        f"👤 My Profile\n\n"
        f"🆔 User ID: {user.id}\n"
        f"👤 Username: @{user.username}\n"
        f"👥 Referrals: {data['referrals']}\n"
        f"⭐ Points: {data['points']}\n"
        f"💰 Reward: {data['reward']} টাকা"
    )

from referral import get_user


def get_profile(user_id, username):
    user = get_user(user_id)

    if not user:
        return "❌ User not found."

    profile_status = "🔓 Unlocked" if user["referrals"] >= 3 else "🔒 Locked"

    premium_status = "🏆 Free Premium" if user["referrals"] >= 150 else "💳 Paid Required"

    text = (
        "👤 Bangladesh Result Hub Profile\n\n"
        f"🆔 User ID : {user_id}\n"
        f"👤 Username : @{username if username else 'None'}\n\n"
        f"👥 Referrals : {user['referrals']}\n"
        f"📂 Profile : {profile_status}\n"
        f"💎 Premium : {premium_status}\n\n"
        "ℹ️ ৩টি রেফার সম্পন্ন হলে Profile Unlock হবে।\n"
        "🏆 ১৫০টি রেফার সম্পন্ন হলে সকল Premium Feature বিনামূল্যে ব্যবহার করতে পারবেন।"
    )

    return text
