# Monte Carlo Risk Simulator

This project simulates stock prices using **Geometric Brownian Motion (GBM)** and estimates **Value-at-Risk (VaR)** for multiple assets.

## Features
- Pulls 5 years of historical stock data from Google Finance
- Calculates daily log returns, drift, and volatility.
- Runs Monte Carlo simulations with 10,000 paths.
- Computes:
  - **VaR (95%)**
  - **Expected Paths and Standard Deviation**
- Visualizes simulated paths vs actual price path.

## Tools
- Python (`numpy`, `pandas`, `matplotlib`)
