from abc import ABC, abstractmethod


class DataSaveInterface(ABC):
    """Abstract class for raw data module."""

    @abstractmethod
    def load(self):
        """Load raw data."""
        pass

    @abstractmethod
    def save(self):
        """Save raw data."""
        pass
