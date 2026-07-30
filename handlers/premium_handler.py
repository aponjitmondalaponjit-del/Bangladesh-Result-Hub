from services.premium_service import (
    premium_active,
)


def my_premium(user):
    return {
        "active": premium_active(user),
        "expire": user.get("premium_end"),
    }


def future_premium():
    return False
