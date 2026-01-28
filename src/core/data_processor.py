import pandas as pd

def process_positions(positions_data):
    """
    Process raw positions data from Kite API into a Pandas DataFrame.

    Args:
        positions_data (dict): The dictionary returned by kite.positions()

    Returns:
        pd.DataFrame: A DataFrame containing 'net' positions.
    """
    net_positions = positions_data.get('net', [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Select relevant columns for our dashboard
    relevant_columns = [
        'tradingsymbol', 'exchange', 'product', 'quantity',
        'average_price', 'last_price', 'pnl', 'm2m'
    ]

    # Ensure all relevant columns exist in the DataFrame
    for col in relevant_columns:
        if col not in df.columns:
            df[col] = 0.0

    return df[relevant_columns]

def calculate_total_mtm(df):
    """
    Calculate the total Mark to Market profit/loss.

    Args:
        df (pd.DataFrame): The processed positions DataFrame.

    Returns:
        float: Total MTM.
    """
    if df.empty:
        return 0.0
    return df['m2m'].sum()
