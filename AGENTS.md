# Agent Guidelines

## Coding Standards
- Follow PEP 8 conventions.
- Use modular architecture: `src/api`, `src/core`, `src/ui`, `src/utils`.
- Maintain a `Mock Mode` in `KiteManager` for development and testing.

## Testing
- Add unit tests for core logic in the `tests/` directory.
- Run tests using `python -m unittest discover tests`.

## Visualizations
- Use `matplotlib` with the `Agg` backend for non-interactive environments.
- Save dashboards as images (e.g., `mtm_dashboard.png`).

## Configuration
- Use environment variables via `python-dotenv`.
- Manage credentials in a `.env` file (ensure it's ignored by git).
