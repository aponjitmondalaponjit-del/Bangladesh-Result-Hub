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
