NOTICES = []


def add_notice(title, message):
    NOTICES.append({
        "title": title,
        "message": message,
    })


def get_notices():
    return NOTICES


def clear_notices():
    NOTICES.clear()


def notice_count():
    return len(NOTICES)
