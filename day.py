from dataclasses import dataclass, field
from pill import Pill
from datetime import datetime

@dataclass(order=True)
class Day:
    sort_index: int = field(init=False, repr=False)
    date: datetime
    pills: list[Pill]
    note: str = None

    def __post_init__(self):
        self.sort_index = self.date

    def __str__(self):
        return f"Date: {self.date}, Pills: {self.pills}, Note: {self.note}"
