from abc import ABC, abstractmethod

class StrategyBase(ABC):
    """
    Abstract Base Class for all trading strategies.
    Provides a standard interface for strategy implementation.
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def entry_signal(self, data):
        """
        Logic for entry signal.
        """
        pass

    @abstractmethod
    def exit_signal(self, data):
        """
        Logic for exit signal.
        """
        pass

    @abstractmethod
    def execute(self, data):
        """
        Main execution logic for the strategy.
        """
        pass
