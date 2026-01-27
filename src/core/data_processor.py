import pandas as pd

class DataProcessor:
    @staticmethod
    def process_positions(positions_data):
        """
        Extracts relevant information from the positions data.
        Returns a pandas DataFrame.
        """
        net_positions = positions_data.get("net", [])
        if not net_positions:
            return pd.DataFrame(columns=["tradingsymbol", "pnl", "m2m"])

        df = pd.DataFrame(net_positions)
        # We only need tradingsymbol, pnl, and m2m for now
        return df[["tradingsymbol", "pnl", "m2m"]]
