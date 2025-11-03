"""Base harvester interface for all data source plugins."""

from abc import ABC, abstractmethod
from builder_harvester.models import RawProfile


class BaseHarvester(ABC):
    """Abstract base class for harvester plugins."""

    @abstractmethod
    def harvest(self, **kwargs) -> list[RawProfile]:
        """
        Harvest profiles from the data source.

        Returns:
            List of RawProfile objects
        """
        pass
