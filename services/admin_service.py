def is_owner(user):
    return False


def is_admin(user):
    return False


def can_publish_notice(user):
    return False


def can_reply_ticket(user):
    return False


def can_manage_users(user):
    return is_owner(user)
