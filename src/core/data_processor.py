import pandas as pd

def process_positions(positions_data):
    """
    Processes the raw positions data from Kite API into a pandas DataFrame.
    """
    net_positions = positions_data.get("net", [])

    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Selecting relevant columns for the dashboard
    relevant_columns = ['tradingsymbol', 'exchange', 'quantity', 'average_price', 'last_price', 'pnl', 'm2m']

    # Ensure all relevant columns exist in the DataFrame
    for col in relevant_columns:
        if col not in df.columns:
            df[col] = 0.0

    return df[relevant_columns]

def get_total_m2m(df):
    """
    Calculates the total M2M from the positions DataFrame.
    """
    if df.empty:
        return 0.0
    return df['m2m'].sum()
