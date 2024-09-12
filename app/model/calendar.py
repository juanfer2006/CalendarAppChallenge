from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar
from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error

from dataclasses import dataclass


@dataclass
class Reminder:
    EMAIL = "email"
    SYSTEM = "system"

    date_time: datetime
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


# TODO: Implement Day class here


# TODO: Implement Calendar class here
