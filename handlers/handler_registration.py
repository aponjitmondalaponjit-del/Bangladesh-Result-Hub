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
)

from handlers.start_handler import start_handler


def register_handlers(app: Application) -> None:
    """
    Register all handlers.
    """

    # Start Command
    app.add_handler(
        CommandHandler(
            "start",
            start_handler,
        )
    )
