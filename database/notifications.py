NOTIFICATIONS = []


def add_notice(data):
    NOTIFICATIONS.append(data)


def active_notices():
    return NOTIFICATIONS


def remove_notice(index):
    if index < len(NOTIFICATIONS):
        NOTIFICATIONS.pop(index)


def clear_notices():
    NOTIFICATIONS.clear()
