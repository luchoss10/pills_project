from .data_save_interface import DataSaveInterface


class RawFileStorage(DataSaveInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        """Load raw data."""
        with open(self.file_path, "r") as file:
            return file.read()

    def save(self, data: str):
        """Save raw data."""
        with open(self.file_path, "w") as file:
            file.write(data)
