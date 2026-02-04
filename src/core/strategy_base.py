from abc import ABC, abstractmethod

class StrategyBase(ABC):
    """
    Abstract Base Class for all trading strategies.
    Provides a standard interface for strategy execution.
    """

    def __init__(self, kite_manager):
        self.km = kite_manager

    @abstractmethod
    def entry(self):
        """
        Logic for entering a trade.
        """
        pass

    @abstractmethod
    def exit(self):
        """
        Logic for exiting a trade.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Main execution loop for the strategy.
        """
        pass
