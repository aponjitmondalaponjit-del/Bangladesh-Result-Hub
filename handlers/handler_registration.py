"""
==========================================================
Bangladesh Result Hub (BRH)

Handler Registration

Version : 1.0.0

Responsibilities:
- Register all bot handlers
- Connect commands
- Connect message handlers
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


def register_handlers(app: Application) -> None:
    """
    Register all handlers.
    """

    # ==========================================
    # Commands
    # ==========================================

    app.add_handler(
        CommandHandler(
            "start",
            start_handler,
        )
    )

    # ==========================================
    # Main Menu Buttons
    # ==========================================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )
