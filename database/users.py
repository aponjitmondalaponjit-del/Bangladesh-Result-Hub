USERS = {}


def get_user(user_id):
    return USERS.get(user_id)


def create_user(user_id):
    if user_id not in USERS:
        USERS[user_id] = {
            "id": user_id,
            "premium": False,
            "referrals": 0,
        }

    return USERS[user_id]


def save_user(user):
    USERS[user["id"]] = user


def all_users():
    return USERS.values()
