def is_profile_unlocked(user):
    return user["referrals"] >= 3


def is_premium(user):
    return user["referrals"] >= 150


def profile_status(user):
    return {
        "profile": is_profile_unlocked(user),
        "premium": is_premium(user),
    }


def can_edit_profile(user):
    return is_profile_unlocked(user)
