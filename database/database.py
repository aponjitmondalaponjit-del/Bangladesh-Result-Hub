import json
import os

DATA_FILE = "user_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_user(user_id):
    data = load_data()
    return data.get(str(user_id))


def add_user(user_id, user_data):
    data = load_data()
    data[str(user_id)] = user_data
    save_data(data)


def update_user(user_id, user_data):
    data = load_data()
    data[str(user_id)] = user_data
    save_data(data)


def user_exists(user_id):
    data = load_data()
    return str(user_id) in data
