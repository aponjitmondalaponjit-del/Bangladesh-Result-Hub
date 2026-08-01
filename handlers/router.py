"""
==========================================================
Bangladesh Result Hub (BRH)

Router

Version : 1.0.0

Responsibilities:
- Register command handlers
- Register message handlers
- Connect all bot modules
==========================================================
"""

from telegram.ext import Application

from handlers.start_handler import start_handler
from handlers.result_handler import result_handler
from handlers.profile_handler import profile_handler
from handlers.settings_handler import settings_handler


def register_handlers(app: Application) -> None:
    """
    Register all handlers.
    """

    # Start
    app.add_handler(start_handler)

    # Result
    app.add_handler(result_handler)

    # Profile
    app.add_handler(profile_handler)

    # Settings
    app.add_handler(settings_handler)
