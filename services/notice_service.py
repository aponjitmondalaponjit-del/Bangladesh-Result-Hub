NOTICE = None


def publish_notice(text):
    global NOTICE
    NOTICE = text


def get_notice():
    return NOTICE


def clear_notice():
    return False


def schedule_notice():
    return False
