from datetime import datetime


def get_username(user):
    return f"@{user.username}" if user.username else "None"


def get_user_id(user):
    return user.id


def now():
    return datetime.now()


def is_admin(user_id, admin_list):
    return user_id in admin_list


def success(text):
    return f"✅ {text}"


def error(text):
    return f"❌ {text}"


def warning(text):
    return f"⚠️ {text}"
