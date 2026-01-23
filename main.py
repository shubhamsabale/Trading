import matplotlib
matplotlib.use('Agg')  # Set the backend before importing any other plotting code

from src.api.kite_manager import KiteManager
from src.core.data_processor import calculate_mtm
from src.ui.dashboard import plot_mtm, display_summary

def main():
    print("Starting Trading Dashboard...")

    # Initialize Kite Manager
    km = KiteManager()

    # Fetch Positions
    print("Fetching positions...")
    positions = km.get_positions()

    # Process Data
    print("Processing data...")
    df = calculate_mtm(positions)

    # Display Summary
    display_summary(df)

    # Plot MTM
    if not df.empty:
        print("Generating MTM graph...")
        plot_mtm(df)

    print("Task completed.")

if __name__ == "__main__":
    main()
