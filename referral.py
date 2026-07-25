import json

DATA_FILE = "user_data.json"


def load_users():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)


def register_user(user_id, username=""):
    users = load_users()

    user_id = str(user_id)

    if user_id not in users:
        users[user_id] = {
            "username": username,
            "referrals": 0,
            "points": 0,
            "reward": 0,
            "referred_by": None
        }
        save_users(users)

    return users[user_id]


def get_user(user_id):
    users = load_users()
    return users.get(str(user_id), None)
