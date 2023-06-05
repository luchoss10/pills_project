from pill import Pill


class day:
    def __init__(self, date, pill: Pill, note: str = None):
        self.date = date
        self.pill = pill
        self.note = note

    def change_date(self, date):
        self.date = date

    def change_pill(self, pill: Pill):
        self.pill = pill

    def change_note(self, note: str):
        self.note = note

    def __str__(self):
        return f"Date: {self.date}, Pill: {self.pill}, Note: {self.note}"
