from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions
from src.ui.dashboard import plot_mtm

def main():
    print("Starting Trading Dashboard...")

    # Initialize Kite Manager
    kite_mgr = KiteManager()

    # Fetch positions
    print("Fetching positions...")
    positions = kite_mgr.get_positions()

    # Process data
    df = process_positions(positions)

    if not df.empty:
        print("Positions found:")
        print(df[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'm2m']])

        # Generate dashboard
        plot_mtm(df)
    else:
        print("No active positions found.")

if __name__ == "__main__":
    main()
