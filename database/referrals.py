REFERRALS = {}


def get_referrals(user_id):
    return REFERRALS.get(user_id, [])


def add_referral(user_id, new_user):
    data = get_referrals(user_id)

    if new_user not in data:
        data.append(new_user)

    REFERRALS[user_id] = data


def referral_count(user_id):
    return len(get_referrals(user_id))


def has_referred(user_id, new_user):
    return new_user in get_referrals(user_id)
