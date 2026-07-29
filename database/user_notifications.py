USER_NOTIFICATION = {}


def notification_enabled(user_id):
    return USER_NOTIFICATION.get(user_id, True)


def set_notification(user_id, status):
    USER_NOTIFICATION[user_id] = status


def reset_notification(user_id):
    USER_NOTIFICATION[user_id] = True
