from database.database import (
    get_user,
    add_user,
    update_user,
    user_exists,
)


def register_user(user_id, username):
    if not user_exists(user_id):
        add_user(user_id, {
            "username": username,
            "referrals": 0,
            "points": 0,
            "reward": 0
        })


def get_user_data(user_id):
    return get_user(user_id)


def add_referral(user_id):
    user = get_user(user_id)

    if user:
        user["referrals"] += 1
        user["points"] += 250

        if user["points"] >= 1500:
            user["reward"] = user["points"] // 1500

        update_user(user_id, user)
