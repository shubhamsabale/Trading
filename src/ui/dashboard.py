import logging
from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions, calculate_total_mtm
from src.ui.plots import plot_mtm_per_instrument

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_dashboard():
    logger.info("Starting Trading Dashboard...")

    try:
        # 1. Initialize Kite Manager
        km = KiteManager()

        # 2. Fetch positions
        logger.info("Fetching current positions...")
        positions_data = km.get_positions()

        # 3. Process data
        df = process_positions(positions_data)

        if df.empty:
            logger.info("No active positions found.")
            return

        # 4. Calculate total MTM
        total_mtm = calculate_total_mtm(df)

        # 5. Display Summary
        print("\n" + "="*50)
        print("CURRENT POSITIONS SUMMARY")
        print("="*50)
        print(df[['tradingsymbol', 'quantity', 'average_price', 'last_price', 'calculated_mtm']])
        print("-" * 50)
        print(f"TOTAL MTM P/L: {total_mtm:.2f}")
        print("="*50 + "\n")

        # 6. Generate MTM Graph
        logger.info("Generating MTM P/L graph...")
        plot_path = plot_mtm_per_instrument(df)
        if plot_path:
            logger.info(f"Graph saved successfully to {plot_path}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run_dashboard()
