import logging
from src.api.kite_manager import KiteManager
from src.core.data_processor import DataProcessor
from src.ui.dashboard import Dashboard
from src.utils.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Trading Dashboard Application")

    if not Config.is_configured():
        logger.error("Kite API not configured and MOCK_MODE is False. Please check your .env file.")
        return

    # Initialize Kite Manager
    kite_manager = KiteManager()

    # Fetch positions
    logger.info("Fetching positions...")
    positions = kite_manager.get_positions()

    # Process data
    logger.info("Processing position data...")
    df = DataProcessor.process_positions(positions)

    if df.empty:
        logger.warning("No net positions found.")
    else:
        logger.info(f"Positions found:\n{df}")

        # Generate Dashboard
        logger.info("Generating MTM dashboard...")
        Dashboard.plot_mtm(df)

    logger.info("Application finished.")

if __name__ == "__main__":
    main()
