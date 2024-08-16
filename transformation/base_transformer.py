# transformation/base_transformer.py

from abc import ABC, abstractmethod

class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, data, source):
        """Transform the data to the desired format."""
        pass
