import matplotlib.pyplot as plt
import pandas as pd

def generate_mtm_graph(df, output_path="mtm_dashboard.png"):
    """
    Generates a bar graph of MTM profit/loss per instrument.
    """
    if df.empty:
        print("No positions to plot.")
        return False

    plt.figure(figsize=(10, 6))

    # Use 'Agg' backend for non-interactive environments as per memory
    plt.switch_backend('Agg')

    # Sort by MTM for better visualization
    df_sorted = df.sort_values(by='calculated_mtm')

    colors = ['green' if x >= 0 else 'red' for x in df_sorted['calculated_mtm']]

    plt.bar(df_sorted['tradingsymbol'], df_sorted['calculated_mtm'], color=colors)

    plt.xlabel('Instrument')
    plt.ylabel('MTM Profit/Loss (INR)')
    plt.title('Mark to Market Profit/Loss per Position')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Dashboard saved to {output_path}")
    return True
