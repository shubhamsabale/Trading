# Agent Instructions

## Project Overview
This is a Python-based algorithmic trading system using Zerodha Kite API.

## Coding Conventions
- Follow PEP 8 style guide.
- Use modular architecture: `api`, `core`, `ui`, `utils`.
- Use `MOCK_MODE` for testing and development.
- Dashboard visualizations should be saved as images (e.g., `mtm_dashboard.png`).

## Testing
- Use `unittest` framework.
- Tests should be located in the `tests/` directory.
- Run tests with `python -m unittest discover tests`.

## Environment
- Dependencies are in `requirements.txt`.
- Configuration is managed via `src/utils/config.py` and environment variables.
