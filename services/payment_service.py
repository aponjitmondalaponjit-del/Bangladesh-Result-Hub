from random import randint


def generate_order_id():
    return f"BRH-{randint(100000,999999)}"


def package_days(month):
    return month * 30


def package_price(month):
    return 25 + (month - 1) * 20


def order_status():
    return "pending"
