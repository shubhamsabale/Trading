import matplotlib.pyplot as plt

def plot_mtm(df, filename='mtm_dashboard.png'):
    """
    Plots a bar chart of MTM profit/loss for each position.
    """
    if df.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(10, 6))
    colors = ['green' if x >= 0 else 'red' for x in df['m2m']]
    plt.bar(df['tradingsymbol'], df['m2m'], color=colors)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Current Positions MTM Dashboard')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Dashboard saved as {filename}")
