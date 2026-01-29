from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions
from src.ui.dashboard import generate_mtm_dashboard, display_summary
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting Kite Position Dashboard Application")

    # 1. Initialize Kite Manager
    km = KiteManager()

    # 2. Fetch positions
    logging.info("Fetching current positions...")
    positions_data = km.get_positions()

    # 3. Process data
    logging.info("Processing position data...")
    df = process_positions(positions_data)

    # 4. Display text summary
    display_summary(df)

    # 5. Generate dashboard visualization
    logging.info("Generating MTM dashboard...")
    generate_mtm_dashboard(df)

    logging.info("Application completed successfully")

if __name__ == "__main__":
    main()
