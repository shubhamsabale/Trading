# Algorithmic Trading System - Kite Connect

A modular Python-based algorithmic trading system for the Indian market using Zerodha's Kite Connect API.

## Features
- **Modular Architecture**: Clean separation between API, core logic, and UI.
- **Kite Manager**: Handles authentication and data fetching with a built-in mock mode.
- **MTM Dashboard**: Visualizes Mark to Market profit/loss for current positions.
- **Mock Mode**: Allows development and testing without live API credentials.

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
1. Copy `.env.example` to `.env`.
2. Update the credentials in `.env` if you have a Kite Connect API key and secret.
3. If credentials are missing, the system defaults to `MOCK_MODE=True`.

## Usage
Run the main application:
```bash
python main.py
```
This will fetch current positions and generate an `mtm_dashboard.png` file in the root directory.

## Testing
Run the unit tests:
```bash
python -m unittest discover tests
```

## Project Structure
- `src/api`: Kite Connect API interactions.
- `src/core`: Data processing and trading logic.
- `src/ui`: Visualizations and dashboard.
- `src/utils`: Configuration and utilities.
