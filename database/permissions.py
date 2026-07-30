PERMISSIONS = {}


def set_permission(level, data):
    PERMISSIONS[level] = data


def get_permission(level):
    return PERMISSIONS.get(level, [])


def has_permission(level, permission):
    return permission in get_permission(level)
