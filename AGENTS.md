# Agent Instructions - Algorithmic Trading System

## Project Overview
This project is an algorithmic trading system using the Zerodha Kite API (kiteconnect library) for the Indian Market (NSE, BSE, MCX).

## Architecture
- `src/api/`: Handles external API calls (Kite Connect).
- `src/core/`: Contains the core logic and data processing.
- `src/ui/`: Responsible for visualizations and dashboarding.
- `src/utils/`: Helper functions and configuration management.
- `main.py`: Entry point of the application.

## Coding Conventions
- Use modular imports.
- Ensure all source directories have `__init__.py`.
- Use `python-dotenv` for managing environment variables.
- Implement a `MOCK_MODE` for testing without live API credentials.

## Verification Steps
- Run tests using: `python -m unittest discover tests`
- Verify dashboard generation by checking `mtm_dashboard.png`.
- Ensure `MOCK_MODE` is functional when credentials are missing.
