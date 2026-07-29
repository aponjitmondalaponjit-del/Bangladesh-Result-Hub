import random


USER_HISTORY = {}


def next_ad(user_id, ads):
    if not ads:
        return None

    seen = USER_HISTORY.get(user_id, [])

    available = [
        ad for ad in ads
        if ad["id"] not in seen
    ]

    if not available:
        USER_HISTORY[user_id] = []
        available = ads

    ad = random.choice(available)

    USER_HISTORY.setdefault(user_id, []).append(ad["id"])

    return ad


def clear_history(user_id):
    USER_HISTORY[user_id] = []
