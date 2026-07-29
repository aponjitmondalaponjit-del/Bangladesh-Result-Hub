def can_unlock_profile(user):
    return user["referrals"] >= 3


def has_free_premium(user):
    return user["referrals"] >= 150


def reward_status(user):
    return {
        "profile": can_unlock_profile(user),
        "premium": has_free_premium(user),
    }


def future_reward():
    return False
