# Stock Market Trading Algorithms

This project aims to build a suite of trading algorithms for the Indian Stock Market (NSE, BSE, MCX) using the Zerodha Kite Connect API.

## Features
- Fetch current positions from Zerodha Kite API.
- Process position data to extract MTM and PNL values.
- Generate a visual dashboard (bar chart) showing MTM profit/loss for each position.
- Supports a mock mode for development without requiring live API credentials.

## Project Structure
- `src/api`: Handles external API connections (KiteManager).
- `src/core`: Contains business logic and data processing.
- `src/ui`: Handles visualization and dashboard generation.
- `src/utils`: Configuration and helper functions.
- `tests`: Unit tests for various components.
- `main.py`: Entry point of the application.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your Kite API credentials:
   ```bash
   cp .env.example .env
   ```
4. Run the application:
   ```bash
   python main.py
   ```
   Note: If no credentials are found, the application defaults to **MOCK MODE**.

## Visualization
The application generates an `mtm_dashboard.png` file in the root directory, showing the Mark to Market profit/loss for all active positions.
