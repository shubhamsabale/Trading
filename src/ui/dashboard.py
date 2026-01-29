import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd

def generate_mtm_dashboard(df, output_path="mtm_dashboard.png"):
    """
    Generates a bar chart showing MTM for each position.
    """
    if df.empty:
        print("No position data available to generate dashboard.")
        return

    plt.figure(figsize=(10, 6))

    # Define colors: Green for profit, Red for loss
    colors = ['g' if x >= 0 else 'r' for x in df['m2m']]

    plt.bar(df['tradingsymbol'], df['m2m'], color=colors)

    plt.xlabel('Instrument')
    plt.ylabel('MTM (Profit/Loss)')
    plt.title('Mark to Market (MTM) Dashboard')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a horizontal line at 0
    plt.axhline(0, color='black', linewidth=0.8)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Dashboard saved to {output_path}")

def display_summary(df):
    """
    Displays a text summary of positions.
    """
    if df.empty:
        print("No positions found.")
        return

    print("\n--- Position Summary ---")
    print(df[['tradingsymbol', 'quantity', 'last_price', 'm2m']])
    print(f"\nTotal MTM: {df['m2m'].sum():.2f}")
    print("------------------------\n")
