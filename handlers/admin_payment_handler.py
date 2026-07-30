from database.payment_orders import (
    get_order,
)


def search_order(order_id):
    return get_order(order_id)


def approve(order):
    order["status"] = "approved"
    return order


def reject(order):
    order["status"] = "rejected"
    return order
