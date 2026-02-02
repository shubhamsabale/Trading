from abc import ABC, abstractmethod

class StrategyBase(ABC):
    """
    Abstract Base Class for all trading strategies.
    Provides a standard interface for strategy implementation.
    """
    def __init__(self, kite_manager):
        self.km = kite_manager
        self.data = None

    @abstractmethod
    def entry_condition(self):
        """
        Define the condition for entering a trade.
        """
        pass

    @abstractmethod
    def exit_condition(self):
        """
        Define the condition for exiting a trade.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Main execution logic for the strategy.
        """
        pass
