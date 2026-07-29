from datetime import datetime, timedelta


def is_premium(user):
    return (
        user.get("premium", False)
        or user.get("referrals", 0) >= 150
    )


def ads_enabled(user):
    if is_premium(user):
        return False

    if user.get("ads_disabled", False):
        expire = user.get("ads_until")

        if expire:
            if datetime.now() < datetime.fromisoformat(expire):
                return False

            user["ads_disabled"] = False
            user["ads_until"] = None

    return True


def ad_duration():
    return 10


def disable_ads(user, days):
    user["ads_disabled"] = True
    user["ads_until"] = (
        datetime.now() + timedelta(days=days)
    ).isoformat()

    return user


def enable_ads(user):
    user["ads_disabled"] = False
    user["ads_until"] = None

    return user
