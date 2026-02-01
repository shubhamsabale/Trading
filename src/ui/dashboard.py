import matplotlib.pyplot as plt
import pandas as pd

# Use 'Agg' backend for non-interactive environments
plt.switch_backend('Agg')

def generate_mtm_chart(df, output_path="mtm_dashboard.png"):
    """
    Generates a bar chart showing MTM for each position.
    """
    if df.empty:
        print("No positions to plot.")
        return

    plt.figure(figsize=(10, 6))
    colors = ['green' if x >= 0 else 'red' for x in df['m2m']]

    plt.bar(df['tradingsymbol'], df['m2m'], color=colors)
    plt.xlabel('Trading Symbol')
    plt.ylabel('MTM Profit/Loss')
    plt.title('Mark to Market (MTM) per Position')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"MTM chart saved to {output_path}")

def generate_exposure_pie_chart(df, output_path="exposure_distribution.png"):
    """
    Generates a pie chart showing the exposure distribution (abs quantity * last_price).
    """
    if df.empty:
        print("No positions for exposure distribution.")
        return

    plt.figure(figsize=(8, 8))

    # Exposure = abs(quantity * last_price)
    exposure = (df['quantity'] * df['last_price']).abs()
    labels = df['tradingsymbol']

    plt.pie(exposure, labels=labels, autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title('Market Exposure Distribution per Position')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Exposure pie chart saved to {output_path}")

def display_summary(df, total_mtm):
    """
    Displays a text summary of the positions and total MTM.
    """
    print("\n--- Position Summary ---")
    if df.empty:
        print("No open positions.")
    else:
        # Displaying with better formatting
        pd.options.display.max_columns = None
        pd.options.display.width = 1000
        print(df.to_string(index=False))
    print(f"\nTotal MTM: {total_mtm:.2f}")
    print("------------------------\n")
