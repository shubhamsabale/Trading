import pandas as pd

def process_positions(positions_data):
    """
    Processes raw positions data from Kite API into a pandas DataFrame.
    Calculates MTM if not already provided or for verification.
    """
    net_positions = positions_data.get('net', [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Calculate MTM manually to ensure consistency
    # MTM = (Last Price - Average Price) * Quantity
    # Note: For short positions, quantity is negative.
    df['calculated_mtm'] = (df['last_price'] - df['average_price']) * df['quantity']

    return df

def calculate_total_mtm(df):
    """Calculates total MTM from the positions DataFrame."""
    if df.empty:
        return 0.0
    # Use calculated_mtm for consistency
    return df['calculated_mtm'].sum()
