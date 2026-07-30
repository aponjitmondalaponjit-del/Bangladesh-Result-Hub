ROUTES = {}


def register(command, handler):
    ROUTES[command] = handler


def get_handler(command):
    return ROUTES.get(command)


def all_routes():
    return ROUTES
