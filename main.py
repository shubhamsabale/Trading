from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions, calculate_total_mtm
from src.ui.dashboard import plot_mtm

def main():
    print("Starting Kite Dashboard Application...")

    # 1. Initialize Kite Manager
    km = KiteManager()

    # 2. Fetch positions
    print("Fetching positions...")
    raw_positions = km.get_positions()

    # 3. Process data
    print("Processing position data...")
    df_positions = process_positions(raw_positions)

    if df_positions.empty:
        print("No net positions found.")
    else:
        print("\nCurrent Net Positions:")
        print(df_positions[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'm2m']])

        total_mtm = calculate_total_mtm(df_positions)
        print(f"\nTotal MTM: {total_mtm:.2f}")

        # 4. Generate Dashboard
        print("\nGenerating MTM Dashboard...")
        plot_mtm(df_positions)

if __name__ == "__main__":
    main()
