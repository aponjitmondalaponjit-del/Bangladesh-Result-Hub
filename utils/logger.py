from datetime import datetime


def log(log_type, message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("brh.log", "a", encoding="utf-8") as file:
        file.write(f"[{time}] [{log_type}] {message}\n")


def user_log(message):
    log("USER", message)


def admin_log(message):
    log("ADMIN", message)


def support_log(message):
    log("SUPPORT", message)


def referral_log(message):
    log("REFERRAL", message)


def error_log(message):
    log("ERROR", message)
