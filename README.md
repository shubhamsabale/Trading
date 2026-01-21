# Algo Trading Repo

This repository is for building an algorithmic trading system using Zerodha Kite API.

## Current Features
- Fetch live positions from Zerodha Kite.
- Generate a plot of Mark-to-Market (MTM) profit/loss.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your Kite API credentials in a `.env` file or as environment variables:
   - `KITE_API_KEY`
   - `KITE_API_SECRET`
   - `KITE_ACCESS_TOKEN` (if already available)
