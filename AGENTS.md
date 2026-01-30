# Project Guidelines for AI Agents

## Architecture
- **Separation of Concerns**: Keep API logic, business logic, and UI logic separate.
- **KiteManager**: Always use `KiteManager` for any interaction with the Kite API. It handles Mock mode automatically.
- **DataFrames**: Use `pandas` DataFrames for data processing to ensure scalability.
- **Visualization**: Use `matplotlib` with the `Agg` backend for generating charts in non-interactive environments.

## Coding Standards
- Follow PEP 8 conventions.
- Use descriptive variable and function names.
- Document functions with docstrings.

## Verification Steps
- Before submitting, ensure that `main.py` runs successfully in mock mode.
- Verify that `mtm_dashboard.png` is generated and contains the expected data.
- Run tests using `python -m unittest discover tests`.
