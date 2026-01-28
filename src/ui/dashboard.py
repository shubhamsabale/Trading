import matplotlib.pyplot as plt
import pandas as pd

def plot_mtm(df, output_path='mtm_dashboard.png'):
    """
    Generate a bar chart of Mark to Market profit/loss for each position.

    Args:
        df (pd.DataFrame): Processed positions DataFrame.
        output_path (str): Path to save the dashboard image.
    """
    if df.empty:
        print("No positions to plot.")
        return

    # Use 'Agg' backend for non-interactive plotting
    plt.switch_backend('Agg')

    # Filter positions with non-zero MTM
    df_plot = df[df['m2m'] != 0].copy()

    if df_plot.empty:
        print("No positions with non-zero MTM to plot.")
        return

    plt.figure(figsize=(10, 6))

    # Sort by MTM for better visualization
    df_plot = df_plot.sort_values(by='m2m', ascending=False)

    # Color bars based on profit/loss
    colors = ['green' if x >= 0 else 'red' for x in df_plot['m2m']]

    bars = plt.bar(df_plot['tradingsymbol'], df_plot['m2m'], color=colors)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss (INR)')
    plt.title('Current Positions MTM Dashboard')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add value labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                 va='bottom' if yval > 0 else 'top', ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Dashboard saved to {output_path}")
    plt.close()
