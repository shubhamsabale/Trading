import matplotlib.pyplot as plt
import pandas as pd

def plot_mtm_per_instrument(df, output_path='mtm_plot.png'):
    """
    Generates a bar chart of MTM P/L per instrument.
    """
    if df.empty:
        print("No positions to plot.")
        return None

    plt.figure(figsize=(10, 6))

    # Sort by MTM for better visualization
    df_sorted = df.sort_values(by='calculated_mtm')

    colors = ['green' if x >= 0 else 'red' for x in df_sorted['calculated_mtm']]

    plt.bar(df_sorted['tradingsymbol'], df_sorted['calculated_mtm'], color=colors)

    plt.xlabel('Instrument')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Mark to Market Profit/Loss per Instrument')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add labels on top of bars
    for i, v in enumerate(df_sorted['calculated_mtm']):
        plt.text(i, v + (50 if v >= 0 else -150), f"{v:.2f}", ha='center', va='bottom' if v >= 0 else 'top')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return output_path
