ADMINS = {}


def add_admin(user_id, level):
    ADMINS[user_id] = level


def admin_level(user_id):
    return ADMINS.get(user_id, 0)


def is_admin(user_id):
    return user_id in ADMINS


def remove_admin(user_id):
    ADMINS.pop(user_id, None)
