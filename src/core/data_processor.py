import pandas as pd

def process_positions(positions_data):
    """
    Processes Kite positions data into a pandas DataFrame and calculates MTM.
    """
    net_positions = positions_data.get("net", [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Calculate MTM manually as per requirements
    # MTM = (Last Price - Average Price) * Quantity
    df['calculated_mtm'] = (df['last_price'] - df['average_price']) * df['quantity']

    return df

def get_total_mtm(df):
    """
    Returns the total MTM from the positions DataFrame.
    """
    if df.empty:
        return 0.0
    return df['calculated_mtm'].sum()
