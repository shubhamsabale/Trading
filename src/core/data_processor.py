import pandas as pd

def calculate_mtm(positions):
    """
    Calculate Mark-to-Market (MTM) profit/loss for positions.
    MTM = (Last Price - Average Price) * Quantity
    """
    net_positions = positions.get("net", [])
    if not net_positions:
        return pd.DataFrame()

    df = pd.DataFrame(net_positions)

    # Ensure necessary columns exist
    required_cols = ['tradingsymbol', 'quantity', 'average_price', 'last_price']
    for col in required_cols:
        if col not in df.columns:
            df[col] = 0

    df['mtm'] = (df['last_price'] - df['average_price']) * df['quantity']
    return df
