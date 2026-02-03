from abc import ABC, abstractmethod

class StrategyBase(ABC):
    """
    Abstract Base Class for all trading strategies.
    """
    def __init__(self, kite_manager):
        self.km = kite_manager

    @abstractmethod
    def entry_signal(self):
        """
        Logic to define the entry point of the strategy.
        """
        pass

    @abstractmethod
    def exit_signal(self):
        """
        Logic to define the exit point of the strategy.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Core execution logic for the strategy.
        """
        pass
