# Agent Instructions

## Project Overview
This is an algorithmic trading system for the Indian Market using the Zerodha Kite API.

## Project Structure
- `src/api/`: Handles interactions with external APIs (Kite Connect).
- `src/core/`: Contains the core business logic and data processing.
- `src/ui/`: Responsible for visualizations and dashboarding.
- `src/utils/`: Utility functions and configuration management.
- `tests/`: Unit and integration tests.

## Coding Conventions
- Use `pandas` for data manipulation.
- Use `matplotlib` with the 'Agg' backend for non-interactive plotting.
- Use `python-dotenv` for managing sensitive credentials via a `.env` file.
- Implement a `MOCK_MODE` to allow development without live API access.

## Verification
- To verify changes, run `python main.py` and check the output.
- Ensure that `mtm_dashboard.png` is generated correctly.
- Run tests using `python -m unittest discover tests`.
