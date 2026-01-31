import pandas as pd

def process_positions(positions_data):
    """
    Process positions data from Kite API and return a DataFrame.
    """
    net_positions = positions_data.get("net", [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # We are interested in tradingsymbol, quantity, last_price, and m2m
    columns_to_keep = ['tradingsymbol', 'exchange', 'quantity', 'average_price', 'last_price', 'pnl', 'm2m']
    df = df[columns_to_keep]

    return df

def calculate_total_mtm(df):
    """
    Calculate total MTM from the positions DataFrame.
    """
    if df.empty:
        return 0.0
    return df['m2m'].sum()
