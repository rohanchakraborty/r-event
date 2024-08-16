# connectors/base_connector.py

from abc import ABC, abstractmethod

class BaseConnector(ABC):
    @abstractmethod
    def fetch_data(self):
        """Fetch data from the source system."""
        pass

    @abstractmethod
    def send_data(self, data):
        """Send data to the target system."""
        pass
