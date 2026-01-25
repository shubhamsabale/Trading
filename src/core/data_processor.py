import pandas as pd

def process_positions(positions_data):
    """
    Processes the raw positions data from Kite API into a pandas DataFrame.
    """
    net_positions = positions_data.get("net", [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Calculate MTM if not already present or for verification
    # MTM = (last_price - average_price) * quantity
    # Note: Kite API already provides 'm2m' and 'pnl'

    return df
