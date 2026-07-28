def verify_referral(referrer_id, user_id):
    return referrer_id != user_id


def duplicate_referral(user_id, referred_users):
    return user_id in referred_users


def detect_fake_referral(user):
    return False


def suspicious_activity(user):
    return False


def ban_fake_referral(user):
    return False
