# Agent Instructions

## Coding Conventions
- Follow PEP 8 style guidelines.
- Use modular architecture: `src/api` for IO, `src/core` for logic, `src/ui` for presentation.
- Always implement a mock mode for any external API integration to facilitate testing and development.
- Use `matplotlib` with the `Agg` backend for generating plots to ensure compatibility with non-interactive environments.

## Core Directives
- Position data processing in `src/core/data_processor.py` should focus on `m2m` and `pnl` fields from the Kite API.
- Dashboard visualizations should clearly distinguish between profit (green) and loss (red).
- Maintain `tests/` and ensure high coverage of core logic.

## Verification Steps
- Run tests: `python -m unittest discover tests`
- Run main application in mock mode: `python main.py`
- Verify artifact generation: `ls mtm_dashboard.png`
