REWARDS = {}


def get_points(user_id):
    return REWARDS.get(user_id, 0)


def add_points(user_id, points):
    REWARDS[user_id] = get_points(user_id) + points


def remove_points(user_id, points):
    total = max(0, get_points(user_id) - points)
    REWARDS[user_id] = total


def reset_points(user_id):
    REWARDS[user_id] = 0
