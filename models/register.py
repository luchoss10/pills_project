from dataclasses import dataclass
from datetime import datetime

from models.pill import Pill

@dataclass
class Register:
    date: datetime
    pill: Pill
    note: str = None

    def __init__(self, date: datetime, pill: Pill, note: str = None):
        self.date = date
        self.pill = pill
        self.note = note

    def change_date(self, date):
        self.date = date

    def change_pill(self, pill: Pill):
        self.pill_list = pill_list

    def change_note(self, note: str):
        self.note = note

    def __str__(self):
        return f"Date: {self.date}, Pill register: {self.pill}, Note: {self.note}"
