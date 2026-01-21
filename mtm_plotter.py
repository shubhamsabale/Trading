import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# Set non-interactive backend
matplotlib.use('Agg')

def plot_mtm(positions, output_file='mtm_plot.png'):
    if not positions or 'net' not in positions:
        print("No positions found to plot.")
        return

    net_positions = positions['net']
    if not net_positions:
        print("Net positions list is empty.")
        return

    df = pd.DataFrame(net_positions)

    # Extract symbol and m2m
    symbols = df['tradingsymbol']
    mtm_values = df['m2m']

    # Create the plot
    plt.figure(figsize=(10, 6))
    colors = ['green' if val >= 0 else 'red' for val in mtm_values]

    bars = plt.bar(symbols, mtm_values, color=colors)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM (Profit/Loss)')
    plt.title('Mark-to-Market (MTM) per Position')

    # Add values on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2),
                 va='bottom' if yval > 0 else 'top', ha='center')

    plt.tight_layout()
    plt.savefig(output_file)
    print(f"MTM plot saved to {output_file}")
    plt.close()

if __name__ == "__main__":
    from kite_utils import KiteManager
    km = KiteManager(mock=True)
    positions = km.get_positions()
    plot_mtm(positions)
