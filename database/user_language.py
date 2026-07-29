USER_LANGUAGE = {}


def get_language(user_id):
    return USER_LANGUAGE.get(user_id, "বাংলা")


def set_language(user_id, language):
    USER_LANGUAGE[user_id] = language


def reset_language(user_id):
    USER_LANGUAGE[user_id] = "বাংলা"
