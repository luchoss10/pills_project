from dataclasses import dataclass

@dataclass
class Pill:
    name: str
    measure: int
    description: str = None

    def __str__(self):
        return f"Pill_name: {self.name}, Measure: {self.measure}mg, description: {self.description}"
