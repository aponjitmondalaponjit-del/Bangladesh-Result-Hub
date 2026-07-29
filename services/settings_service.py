def notification_enabled(user):
    return user.get("notification", True)


def set_notification(user, status):
    user["notification"] = status
    return user


def get_settings(user):
    return {
        "notification": notification_enabled(user),
        "language": user.get("language", "বাংলা"),
    }


def future_settings():
    return False
