USER_PROFILE = {}


def get_profile(user_id):
    return USER_PROFILE.get(user_id)


def save_profile(user_id, profile):
    USER_PROFILE[user_id] = profile


def update_profile(user_id, key, value):
    profile = get_profile(user_id) or {}
    profile[key] = value
    save_profile(user_id, profile)


def delete_profile(user_id):
    USER_PROFILE.pop(user_id, None)
