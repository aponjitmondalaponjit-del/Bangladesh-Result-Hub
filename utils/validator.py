def valid_username(username):
    return bool(username)


def valid_roll(roll):
    return str(roll).isdigit()


def valid_registration(registration):
    return str(registration).isdigit()


def valid_referral(referrer, new_user):
    return referrer != new_user


def valid_language(language):
    return language in [
        "bn",
        "en",
        "hi",
        "ar"
    ]
