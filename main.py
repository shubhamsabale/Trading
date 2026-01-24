import sys
import logging
from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions, get_total_mtm
from src.ui.dashboard import generate_mtm_graph

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Trading Dashboard...")

    # 1. Initialize Kite Manager
    km = KiteManager()

    # 2. Fetch current positions
    logger.info("Fetching current positions...")
    positions = km.get_positions()

    # 3. Process positions data
    logger.info("Processing data...")
    df = process_positions(positions)

    if df.empty:
        logger.warning("No positions found.")
        return

    # 4. Display summary
    total_mtm = get_total_mtm(df)
    logger.info(f"Total MTM: {total_mtm:.2f}")

    print("\nCurrent Positions Summary:")
    print(df[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'calculated_mtm']])
    print(f"\nTotal Portfolio MTM: {total_mtm:.2f}")

    # 5. Generate Graph
    logger.info("Generating MTM Dashboard...")
    generate_mtm_graph(df)

    logger.info("Dashboard updated successfully.")

if __name__ == "__main__":
    main()
