"""
==========================================================
Bangladesh Result Hub (BRH)

Result Formatter

Version : 1.0.0

Responsibilities:
- Format result for Telegram
- Format error messages
- Format premium messages
- Build clean result output
==========================================================
"""

from __future__ import annotations

from typing import Any


LINE = "━━━━━━━━━━━━━━━━━━━━"


def format_result(data: dict[str, Any]) -> str:
    """
    Format student result for Telegram.
    """

    return (
        f"🎓 Bangladesh Result Hub\n"
        f"{LINE}\n"
        f"👤 Name : {data.get('name', 'N/A')}\n"
        f"🆔 Roll : {data.get('roll', 'N/A')}\n"
        f"📝 Registration : {data.get('registration', 'N/A')}\n"
        f"📚 Exam : {data.get('exam', 'N/A')}\n"
        f"🏫 Board : {data.get('board', 'N/A')}\n"
        f"📅 Year : {data.get('year', 'N/A')}\n"
        f"⭐ GPA : {data.get('gpa', 'N/A')}\n"
        f"{LINE}\n"
        f"© Bangladesh Result Hub"
    )


def format_error(message: str) -> str:
    """
    Format error message.
    """

    return (
        "❌ Error\n"
        f"{LINE}\n"
        f"{message}"
    )


def format_not_found() -> str:
    """
    Result not found.
    """

    return (
        "❌ Result not found.\n"
        "Please check your information and try again."
    )


def format_premium_required() -> str:
    """
    Premium required message.
    """

    return (
        "💎 Premium Feature\n"
        f"{LINE}\n"
        "Please activate Premium to use this feature."
    )


def format_maintenance() -> str:
    """
    Maintenance message.
    """

    return (
        "🚧 System Maintenance\n"
        "Please try again later."
    )
