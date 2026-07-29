DEFAULT_LANGUAGE = "বাংলা"


def get_language(user):
    return user.get("language", DEFAULT_LANGUAGE)


def set_language(user, language):
    user["language"] = language
    return user


def supported_languages():
    return [
        "বাংলা",
        "English",
        "हिन्दी",
        "العربية",
    ]


def future_language_pack():
    return False
