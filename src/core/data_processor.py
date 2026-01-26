import pandas as pd

def process_positions(positions_data):
    """
    Processes Kite positions data into a pandas DataFrame.
    """
    net_positions = positions_data.get('net', [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)
    return df[['tradingsymbol', 'quantity', 'm2m', 'pnl']]
