import matplotlib.pyplot as plt
import os

def plot_mtm(df, output_path="mtm_dashboard.png"):
    """
    Plots the MTM for each position.
    """
    if df.empty:
        print("No positions to plot.")
        return

    plt.figure(figsize=(10, 6))
    colors = ['green' if x >= 0 else 'red' for x in df['mtm']]
    plt.bar(df['tradingsymbol'], df['mtm'], color=colors)

    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Mark-to-Market (MTM) Dashboard')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the plot
    plt.savefig(output_path)
    print(f"Dashboard saved to {output_path}")
    plt.close()

def display_summary(df):
    """
    Displays a text summary of the positions.
    """
    if df.empty:
        print("No positions found.")
        return

    print("\n--- Position Summary ---")
    print(df[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'mtm']].to_string(index=False))
    total_mtm = df['mtm'].sum()
    print(f"\nTotal MTM: {total_mtm:.2f}")
    print("------------------------\n")
