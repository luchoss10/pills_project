from pill import Pill
from datetime import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class DayRecord:

    date: datetime
    pill_list: List[Pill]
    note: str = None

    def __init__(self, date: datetime, pill_list: List[Pill], note: str = None):
        self.date = date
        if isinstance(pill_list, Pill):
            pill_list = [pill_list]
        self.pill_list = pill_list
        self.note = note

    def change_date(self, date):
        self.date = date

    def change_pill_list(self, pill_list: Pill):
        self.pill_list = pill_list

    def change_note(self, note: str):
        self.note = note

    def __str__(self):
        pills_in_day = [pill.name for pill in self.pill_list]
        return f"Date: {self.date}, Pill register: {pills_in_day}, Note: {self.note}"
