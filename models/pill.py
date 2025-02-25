from dataclasses import dataclass


@dataclass
class Pill:
    name: str
    measure: int
    description: str = None
    frequency_day: int = 1

    def change_name(self, name: str):
        self.name = name

    def change_measure(self, measure: int):
        self.measure = measure

    def change_description(self, description: str):
        self.description = description

    def delete_description(self):
        self.description = None

    def change_frequency_day(self, frequency_day: int):
        self.frequency_day = frequency_day

    def reset_frequency_day(self):
        self.frequency_day = 1

    def __str__(self):
        return f"Pill_name: {self.name}, Measure: {self.measure}mg, description: {self.description}, frequency_day: {self.frequency_day}"
