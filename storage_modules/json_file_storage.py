import json

from .data_save_interface import DataSaveInterface


class JsonFileStorage(DataSaveInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        """Load raw data."""
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save(self, data: str):
        """Save raw data."""
        with open(self.file_path, "w") as file:
            json.dump(data, file)
