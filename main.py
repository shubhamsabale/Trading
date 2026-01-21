from kite_utils import KiteManager
from mtm_plotter import plot_mtm
import os

def main():
    # Attempt to initialize KiteManager
    # It will automatically switch to mock mode if credentials are missing
    km = KiteManager()

    print(f"Using {'Mock' if km.mock else 'Live'} Kite Client")

    # Fetch positions
    print("Fetching live positions...")
    positions = km.get_positions()

    if positions:
        print(f"Successfully fetched {len(positions.get('net', []))} net positions.")
        # Plot MTM
        plot_mtm(positions)
    else:
        print("Failed to fetch positions.")

if __name__ == "__main__":
    main()
