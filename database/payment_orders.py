PAYMENT_ORDERS = {}


def create_order(order):
    PAYMENT_ORDERS[order["order_id"]] = order


def get_order(order_id):
    return PAYMENT_ORDERS.get(order_id)


def save_order(order):
    PAYMENT_ORDERS[order["order_id"]] = order


def all_orders():
    return PAYMENT_ORDERS.values()
