# Algorithmic Trading Project - Kite Connect

## Project Overview
This project aims to build stock market trading algorithms for the Indian market using the Zerodha Kite Connect API.

## Directory Structure
- `src/api`: Handles interaction with the Kite API.
- `src/core`: Core logic and data processing.
- `src/ui`: Visualization and dashboard components.
- `src/utils`: Configuration and helper functions.
- `tests`: Unit and integration tests.

## Coding Conventions
- Follow PEP 8 style guide.
- Use modular design.
- Include docstrings for all functions and classes.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Set up `.env` file based on `.env.example`.
3. Run the application: `python main.py`

## Development Notes
- Use `MOCK_MODE=True` in `.env` to test without real API credentials.
- Dashboard MTM graph is saved as `mtm_dashboard.png`.
