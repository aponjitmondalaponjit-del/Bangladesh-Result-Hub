from datetime import datetime, timedelta


def activate(user, months):
    user["premium"] = True
    user["premium_start"] = datetime.now().isoformat()
    user["premium_end"] = (
        datetime.now() + timedelta(days=months * 30)
    ).isoformat()
    return user


def premium_active(user):
    if not user.get("premium"):
        return False

    return datetime.now() < datetime.fromisoformat(
        user["premium_end"]
    )
