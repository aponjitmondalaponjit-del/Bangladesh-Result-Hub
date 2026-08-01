"""
==========================================================
Bangladesh Result Hub (BRH)

Validation Utilities

Version : 1.0.0
==========================================================
"""

from __future__ import annotations

import re

SUPPORTED_EXAMS = {
    "SSC",
    "HSC",
    "DAKHIL",
    "ALIM",
    "TECHNICAL",
}

SUPPORTED_BOARDS = {
    "DHAKA",
    "RAJSHAHI",
    "JESSORE",
    "CHITTAGONG",
    "COMILLA",
    "BARISAL",
    "SYLHET",
    "DINAJPUR",
    "MYMENSINGH",
    "MADRASA",
    "TECHNICAL",
}


def clean_text(text: str) -> str:
    """
    Remove extra spaces and normalize text.
    """
    if text is None:
        return ""

    return str(text).strip()


def normalize(text: str) -> str:
    """
    Convert text to uppercase.
    """
    return clean_text(text).upper()


def is_empty(value: str) -> bool:
    """
    Check empty string.
    """
    return clean_text(value) == ""


def is_valid_roll(roll: str) -> bool:
    """
    Roll number validation.
    """
    roll = clean_text(roll)

    if not roll.isdigit():
        return False

    return 1 <= len(roll) <= 10


def is_valid_registration(registration: str) -> bool:
    """
    Registration validation.
    """
    registration = clean_text(registration)

    if not registration.isdigit():
        return False

    return 6 <= len(registration) <= 12


def is_valid_exam(exam: str) -> bool:
    """
    Check supported examination.
    """
    return normalize(exam) in SUPPORTED_EXAMS


def is_valid_board(board: str) -> bool:
    """
    Check supported education board.
    """
    return normalize(board) in SUPPORTED_BOARDS


def is_valid_year(year: int | str) -> bool:
    """
    Validate examination year.
    """
    try:
        year = int(year)
    except Exception:
        return False

    return 1990 <= year <= 2100


def is_valid_phone(phone: str) -> bool:
    """
    Bangladesh phone validation.
    """
    phone = clean_text(phone)

    pattern = r"^(?:\+8801|8801|01)[3-9]\d{8}$"

    return bool(re.fullmatch(pattern, phone))


def is_valid_transaction_id(txid: str) -> bool:
    """
    Validate transaction id.
    """
    txid = clean_text(txid)

    return len(txid) >= 8


def is_valid_order_id(order_id: str) -> bool:
    """
    Validate BRH Order ID.

    Example:
        BRH-572941
    """
    order_id = normalize(order_id)

    pattern = r"^BRH-\d{6}$"

    return bool(re.fullmatch(pattern, order_id))


def is_positive_number(value) -> bool:
    """
    Check positive number.
    """
    try:
        return int(value) > 0
    except Exception:
        return False
