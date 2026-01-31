from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions, calculate_total_mtm
from src.ui.dashboard import plot_mtm, display_summary

def main():
    print("Initializing Trading Dashboard...")

    # 1. Initialize Kite Manager
    km = KiteManager()

    # 2. Fetch positions
    print("Fetching position data...")
    positions = km.get_positions()

    # 3. Process positions
    df = process_positions(positions)

    if not df.empty:
        # 4. Display summary
        display_summary(df)

        # 5. Plot MTM
        print("Generating MTM Dashboard...")
        plot_mtm(df)
    else:
        print("No positions found to display.")

if __name__ == "__main__":
    main()
