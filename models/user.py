from dataclasses import dataclass
from typing import List

from models.register import Register
from models.pill import Pill


@dataclass
class User:
    name: str
    age: int
    _streak_days: int = 0
    pills: List[Pill] = None
    history: List[Register] = None

    def change_name(self, name: str):
        self.name = name

    def change_age(self, age: int):
        self.age = age

    def add_streak_day(self):
        self._streak_days += 1

    def reset_streak_day(self):
        self._streak_days = 0

    def get_streak_days(self):
        return self._streak_days

    def add_day_record(self, register: Register):
        if not self.history:
            self.history = []
        self.history.append(register)

    def get_history(self):
        return self.history

    def add_pill(self, pill: Pill):
        if not self.pills:
            self.pills = []
        self.pills.append(pill)

    def delete_pill(self, pill: Pill):
        self.pills.remove(pill)

    def get_pills(self):
        return self.pills

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Streak days: {self._streak_days}"
