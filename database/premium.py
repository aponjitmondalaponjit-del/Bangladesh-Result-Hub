PREMIUM_USERS = {}


def is_premium(user_id):
    return PREMIUM_USERS.get(user_id, False)


def enable_premium(user_id):
    PREMIUM_USERS[user_id] = True


def disable_premium(user_id):
    PREMIUM_USERS[user_id] = False


def premium_users():
    return PREMIUM_USERS
