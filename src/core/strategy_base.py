class StrategyBase:
    """
    Base class for all trading strategies.
    """
    def __init__(self, name):
        self.name = name

    def on_tick(self, tick):
        """
        Called when a new tick is received.
        """
        pass

    def execute(self):
        """
        Main execution logic for the strategy.
        """
        pass
