# Algorithmic Trading Dashboard

This project is an algorithmic trading system using the Zerodha Kite API for the Indian Market (NSE, BSE, MCX).

## Features
- Modular architecture for scalability.
- Fetch and display current positions.
- Visualize Mark to Market (MTM) profit/loss using a bar chart.
- Mock mode for development without live API access.

## Project Structure
- `src/api/`: Handles Kite API connection and data retrieval.
- `src/core/`: Contains business logic and data processing.
- `src/ui/`: Manages visualization and dashboard output.
- `src/utils/`: Configuration and helper utilities.
- `main.py`: Entry point for the application.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables in a `.env` file (see `.env.example`).
3. Run the dashboard:
   ```bash
   python main.py
   ```

## License
MIT
