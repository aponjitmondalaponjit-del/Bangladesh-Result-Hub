PREMIUM_HISTORY = []


def add_history(data):
    PREMIUM_HISTORY.append(data)


def get_history(user_id):
    return [
        i for i in PREMIUM_HISTORY
        if i["user_id"] == user_id
    ]


def all_history():
    return PREMIUM_HISTORY
