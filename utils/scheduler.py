from datetime import datetime


def result_scheduler():
    return "Result Scheduler Ready"


def notice_scheduler():
    return "Notice Scheduler Ready"


def leaderboard_scheduler():
    return "Leaderboard Scheduler Ready"


def daily_reset():
    return datetime.now().day


def weekly_reset():
    return datetime.now().isocalendar().week


def monthly_reset():
    return datetime.now().month
