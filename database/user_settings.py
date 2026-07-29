USER_SETTINGS = {}


def get_settings(user_id):
    return USER_SETTINGS.get(user_id, {})


def save_settings(user_id, settings):
    USER_SETTINGS[user_id] = settings


def update_setting(user_id, key, value):
    data = get_settings(user_id)
    data[key] = value
    save_settings(user_id, data)


def reset_settings(user_id):
    USER_SETTINGS[user_id] = {}
