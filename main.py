from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions
from src.ui.dashboard import plot_mtm

def main():
    print("Initializing Kite Manager...")
    kite_mgr = KiteManager()

    print("Fetching positions...")
    positions = kite_mgr.get_positions()

    print("Processing position data...")
    df = process_positions(positions)

    if not df.empty:
        print("Positions summary:")
        print(df)

        print("Generating MTM dashboard...")
        plot_mtm(df)
    else:
        print("No active positions found.")

if __name__ == "__main__":
    main()
