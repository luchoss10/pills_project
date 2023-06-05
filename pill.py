class Pill:
    def __init__(self, name: str, measure: int, description: str = None):
        self.name = name
        self.measure = measure
        self.description = description

    def change_name(self, name: str):
        self.name = name

    def change_measure(self, measure: int):
        self.measure = measure

    def change_description(self, description: str):
        self.description = description

    def delete_description(self):
        self.description = None

    def __str__(self):
        return f"Pill_name: {self.name}, Measure: {self.measure}mg, description: {self.description}"
