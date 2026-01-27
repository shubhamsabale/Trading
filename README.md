# Algorithmic Trading System with Zerodha Kite

This project is an algorithmic trading system for the Indian Market (NSE, BSE, MCX) using the Zerodha Kite Connect API.

## Current Features
- Dashboard to fetch and display current position data.
- Visualization of Mark to Market (MTM) profit/loss as a graph.
- Mock mode for development without actual API credentials.

## Project Structure
- `src/api/`: Handles Kite API interactions.
- `src/core/`: Contains business logic and data processing.
- `src/ui/`: Handles visualization and dashboard generation.
- `src/utils/`: Configuration and helper utilities.
- `main.py`: Main entry point of the application.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your API keys in a `.env` file (copy from `.env.example`).
3. Run the application:
   ```bash
   python main.py
   ```

## Mock Mode
By default, the application runs in `MOCK_MODE=True`, which uses sample data. Set `MOCK_MODE=False` in your `.env` file to use the actual Kite API.
