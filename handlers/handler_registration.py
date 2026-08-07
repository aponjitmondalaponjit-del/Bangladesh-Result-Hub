"""
==========================================================
Bangladesh Result Hub (BRH)

Handler Registration

Version : 1.0.0

Responsibilities:
- Register all bot handlers
- Commands
- Main Menu
==========================================================
"""

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from handlers.start_handler import start_handler
from handlers.message_handler import message_handler

from handlers.settings_handler import settings_handler
from handlers.support_handler import support_handler
from handlers.premium_handler import premium_handler


def register_handlers(app: Application):
    """
    Register all handlers.
    """

    # ==========================
    # Commands
    # ==========================

    app.add_handler(
        CommandHandler(
            "start",
            start_handler,
        )
    )

    app.add_handler(
        CommandHandler(
            "settings",
            settings_handler,
        )
    )

    app.add_handler(
        CommandHandler(
            "support",
            support_handler,
        )
    )

    app.add_handler(
        CommandHandler(
            "premium",
            premium_handler,
        )
    )

    # ==========================
    # Text Buttons
    # ==========================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )
