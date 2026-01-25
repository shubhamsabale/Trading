import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

def plot_mtm(df):
    """
    Plots a bar chart of MTM for each position.
    """
    if df.empty:
        print("No positions to plot.")
        return

    plt.figure(figsize=(10, 6))
    colors = ['green' if x >= 0 else 'red' for x in df['m2m']]
    plt.bar(df['tradingsymbol'], df['m2m'], color=colors)
    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Mark to Market (MTM) Dashboard')
    plt.axhline(0, color='black', linewidth=0.8)

    # Save the plot
    plt.savefig('mtm_dashboard.png')
    print("Dashboard saved as mtm_dashboard.png")
    plt.close()
