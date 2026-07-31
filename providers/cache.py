CACHE = {}


def save(key, value):
    CACHE[key] = value


def get(key):
    return CACHE.get(key)


def clear():
    CACHE.clear()
