from src.api.kite_manager import KiteManager
from src.core.data_processor import process_positions, calculate_total_mtm
from src.ui.dashboard import generate_mtm_chart, generate_exposure_pie_chart, display_summary

def main():
    # Initialize Kite Manager
    km = KiteManager()

    # Fetch positions
    positions_data = km.get_positions()

    # Process positions
    df = process_positions(positions_data)

    # Calculate Total MTM
    total_mtm = calculate_total_mtm(df)

    # Display Summary
    display_summary(df, total_mtm)

    # Generate Charts
    generate_mtm_chart(df)
    generate_exposure_pie_chart(df)

if __name__ == "__main__":
    main()
