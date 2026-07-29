LANGUAGES = [
    "বাংলা",
    "English",
    "हिन्दी",
    "العربية",
]


def get_languages():
    return LANGUAGES


def default_language():
    return "বাংলা"


def add_language(name):
    if name not in LANGUAGES:
        LANGUAGES.append(name)

    return LANGUAGES
