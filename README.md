# Algorithmic Trading System

An algorithmic trading system using Zerodha Kite API for the Indian Market.

## Project Structure
- `src/api`: Kite API interaction.
- `src/core`: Data processing and trading logic.
- `src/utils`: Utilities and configuration.
- `src/ui`: Dashboard and visualization.
- `main.py`: Application entry point.
- `tests`: Unit and integration tests.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment variables in `.env` (use `.env.example` as a template).
3. Run the dashboard: `python main.py`

## Features
- Fetches current positions from Kite API.
- Supports Mock Mode for development without API keys.
- Calculates and visualizes MTM (Mark-to-Market) profit/loss.
