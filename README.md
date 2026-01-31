# Kite Algo Trading

An algorithmic trading system using the Zerodha Kite API for the Indian Market.

## Features
- Modular architecture (API, Core, UI, Utils).
- Fetch current position data from Kite API.
- Mock mode for development without actual API keys.
- Position summary dashboard with MTM profit/loss visualization.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables in `.env` (refer to `.env.example`).
3. Run the application:
   ```bash
   python main.py
   ```

## Project Structure
- `src/api`: Handles communication with Zerodha Kite API.
- `src/core`: Contains business logic and data processing.
- `src/ui`: Manages visualization and user interface components.
- `src/utils`: Helper functions and configuration management.
- `main.py`: Main entry point of the application.
