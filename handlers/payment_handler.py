from services.payment_service import (
    generate_order_id,
    package_price,
)


def create_payment(month):
    return {
        "order_id": generate_order_id(),
        "month": month,
        "price": package_price(month),
        "status": "pending",
    }


def future_payment():
    return False
