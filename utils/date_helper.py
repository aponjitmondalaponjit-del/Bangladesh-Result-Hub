"""
==========================================================
Bangladesh Result Hub (BRH)

Date Helper Utilities

Version : 1.0.0

Responsibilities:
- Current date/time handling
- Date formatting
- Year validation
- Day calculation
- Premium expiry calculation
==========================================================
"""

from __future__ import annotations

from datetime import datetime, timedelta, date


DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_current_date() -> date:
    """
    Return current date.
    """

    return datetime.now().date()


def get_current_datetime() -> datetime:
    """
    Return current datetime.
    """

    return datetime.now()


def format_date(value: date | datetime) -> str:
    """
    Convert date object to readable format.
    """

    if isinstance(value, datetime):
        value = value.date()

    return value.strftime(DATE_FORMAT)


def format_datetime(value: datetime) -> str:
    """
    Convert datetime object to string.
    """

    return value.strftime(DATETIME_FORMAT)


def parse_date(value: str) -> date | None:
    """
    Convert string date into date object.
    """

    try:
        return datetime.strptime(
            value,
            DATE_FORMAT
        ).date()

    except Exception:
        return None


def is_valid_year(year: int | str) -> bool:
    """
    Validate examination year.
    """

    try:
        year = int(year)

    except Exception:
        return False

    current_year = datetime.now().year

    return 1990 <= year <= current_year + 5


def days_between(start: date, end: date) -> int:
    """
    Calculate days between two dates.
    """

    return (end - start).days


def add_days(start: date, days: int) -> date:
    """
    Add days to date.
    """

    return start + timedelta(days=days)


def premium_expiry_date(days: int = 30) -> date:
    """
    Generate premium expiry date.

    Default:
        30 days
    """

    return get_current_date() + timedelta(days=days)


def is_expired(expiry_date: date) -> bool:
    """
    Check expiry status.
    """

    return get_current_date() > expiry_date


def remaining_days(expiry_date: date) -> int:
    """
    Calculate remaining days.
    """

    remaining = (expiry_date - get_current_date()).days

    if remaining < 0:
        return 0

    return remaining
