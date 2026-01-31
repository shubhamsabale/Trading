import matplotlib.pyplot as plt
from src.utils.config import Config

def plot_mtm(df):
    """
    Generate a bar chart for MTM profit/loss per position.
    """
    if df.empty:
        print("No positions to plot.")
        return

    # Use 'Agg' backend for non-interactive environments
    plt.switch_backend('Agg')

    plt.figure(figsize=(10, 6))

    # Define colors: green for profit, red for loss
    colors = ['green' if x >= 0 else 'red' for x in df['m2m']]

    plt.bar(df['tradingsymbol'], df['m2m'], color=colors)

    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM (INR)')
    plt.title('Mark to Market Profit/Loss per Position')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(Config.MTM_DASHBOARD_PATH)
    print(f"Dashboard saved to {Config.MTM_DASHBOARD_PATH}")
    plt.close()

def display_summary(df):
    """
    Print a summary of positions to the console.
    """
    if df.empty:
        print("No active positions.")
        return

    print("\n--- Position Summary ---")
    print(df[['tradingsymbol', 'quantity', 'last_price', 'm2m']].to_string(index=False))
    print("-" * 25)
    print(f"Total MTM: {df['m2m'].sum():.2f}")
    print("-" * 25)
