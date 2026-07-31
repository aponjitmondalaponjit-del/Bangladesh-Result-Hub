"""
==========================================================
Bangladesh Result Hub (BRH)
Result Service

Version : 1.0.0
Status  : Development

This service is the central engine of BRH Bot.

Responsibilities:
- Validate requests
- Select provider
- Handle cache
- Fetch result
- Format result
- Notification logic
- Premium check
- Search history
==========================================================
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from providers.educationboard import EducationBoardProvider
from providers.madrasaboard import MadrasaBoardProvider
from providers.technicalboard import TechnicalBoardProvider
from providers.cache import CacheProvider

logger = logging.getLogger(__name__)


class ResultService:
    """
    Central Result Service.

    Every result request passes through this service.

    Flow:

        User
          │
          ▼
      Validation
          │
          ▼
      Provider Select
          │
          ▼
      Cache Check
          │
          ▼
      Fetch Result
          │
          ▼
      Formatter
          │
          ▼
      Telegram Response
    """

    DEFAULT_TIMEOUT = 30
    MAX_RETRY = 3
    CACHE_ENABLED = True
    CACHE_EXPIRE_SECONDS = 600

    def __init__(self) -> None:
        """
        Initialize Result Service.
        """

        self.started_at = datetime.utcnow()

        self.providers = {
            "SSC": EducationBoardProvider(),
            "HSC": EducationBoardProvider(),
            "DAKHIL": MadrasaBoardProvider(),
            "ALIM": MadrasaBoardProvider(),
            "TECHNICAL": TechnicalBoardProvider(),
        }

        self.cache = CacheProvider()

        logger.info("ResultService initialized successfully.")

    @property
    def available_exams(self) -> list[str]:
        """
        Return supported examinations.
        """

        return list(self.providers.keys())

    def provider_exists(self, exam: str) -> bool:
        """
        Check provider availability.
        """

        return exam.upper() in self.providers

    def get_provider(self, exam: str) -> Any:
        """
        Return provider instance.

        Raises:
            ValueError
        """

        exam = exam.upper()

        if exam not in self.providers:
            raise ValueError(f"No provider found for '{exam}'")

        return self.providers[exam]

    def is_cache_enabled(self) -> bool:
        """
        Return cache status.
        """

        return self.CACHE_ENABLED

    def get_cache(self) -> CacheProvider:
        """
        Return cache provider.
        """

        return self.cache
