ORDER_HISTORY = []


def save_order(order):
    ORDER_HISTORY.append(order)


def user_orders(user_id):
    return [
        i for i in ORDER_HISTORY
        if i["user_id"] == user_id
    ]


def all_orders():
    return ORDER_HISTORY
