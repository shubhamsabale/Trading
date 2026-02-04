import pandas as pd

def process_positions(positions_data):
    """
    Processes the raw positions data from Kite API and returns a DataFrame.
    """
    net_positions = positions_data.get("net", [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)
    # Calculate Exposure: |Quantity * Last Price|
    df['exposure'] = (df['quantity'] * df['last_price']).abs()

    # Selecting relevant columns
    cols = ['tradingsymbol', 'exchange', 'quantity', 'last_price', 'm2m', 'pnl', 'exposure']
    df = df[cols]

    return df

def calculate_total_mtm(df):
    """
    Calculates the total MTM from the positions DataFrame.
    """
    if df.empty:
        return 0.0
    return df['m2m'].sum()
