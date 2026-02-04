import matplotlib.pyplot as plt
import pandas as pd

def generate_mtm_chart(df, output_path="mtm_dashboard.png"):
    """
    Generates a bar chart showing MTM for each position.
    """
    if df.empty:
        print("No positions to plot.")
        return

    # Use 'Agg' backend for non-interactive environments
    plt.switch_backend('Agg')

    plt.figure(figsize=(10, 6))
    colors = ['green' if x >= 0 else 'red' for x in df['m2m']]

    bars = plt.bar(df['tradingsymbol'], df['m2m'], color=colors)

    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}',
                 va='bottom' if yval > 0 else 'top', ha='center', fontsize=9)

    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Mark to Market (MTM) per Position')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"MTM chart saved to {output_path}")

def generate_exposure_chart(df, output_path="exposure_distribution.png"):
    """
    Generates a pie chart showing exposure distribution by symbol.
    """
    if df.empty:
        print("No positions to plot.")
        return

    # Use 'Agg' backend for non-interactive environments
    plt.switch_backend('Agg')

    plt.figure(figsize=(8, 8))
    plt.pie(df['exposure'], labels=df['tradingsymbol'], autopct='%1.1f%%', startangle=140)
    plt.title('Exposure Distribution per Position')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Exposure distribution chart saved to {output_path}")

def display_summary(df, total_mtm):
    """
    Displays a text summary of the positions and total MTM.
    """
    print("\n--- Position Summary ---")
    if df.empty:
        print("No open positions.")
    else:
        print(df.to_string(index=False))
    print(f"\nTotal MTM: {total_mtm:.2f}")
    print("------------------------\n")
