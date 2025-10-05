# Monte Carlo Risk Simulator

A Python-based financial risk analysis tool that uses **Geometric Brownian Motion (GBM)** to simulate stock price paths and calculate **Value-at-Risk (VaR)** for portfolio risk management.

## Overview

This project simulates thousands of potential stock price trajectories using Monte Carlo methods based on historical price data. It provides risk metrics including:
- Average expected price paths
- Standard deviation bounds
- 95% Value-at-Risk (VaR) estimates
- Comparison with actual market performance

## Features

- **10,000 Monte Carlo Simulations** per stock for robust statistical analysis
- **Geometric Brownian Motion** modeling with drift and volatility parameters
- **Historical Data Analysis** using 5 years of daily closing prices
- **Risk Metrics**: 95% VaR calculation for downside risk assessment
- **Visualization**: Comprehensive plots comparing simulated vs. actual price paths
- **Multi-Asset Support**: Currently tracks AAPL, GS, MSFT, and CAT

## Installation

### Prerequisites
- Python 3.7 or higher

### Required Libraries
```bash
pip install pandas numpy matplotlib
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository:**
```bash
git clone https://github.com/JoseOC042023/Monte-Carlo-Simulation-Stocks.git
cd Monte-Carlo-Simulation-Stocks
```

2. **Ensure data file is present:**
   - The CSV file `AAPL_GS_MSFT_CAT_5_Year_Close_Price_Data - Static Data.csv` should be in the project directory
   - Data should contain daily closing prices with DATE column and ticker columns

3. **Run the simulation:**
```bash
python Stock_Monte_Sim.py
```

4. **View results:**
   - Two matplotlib figures will display:
     - **Figure 1**: Mean, Standard Deviation, VaR paths, and actual prices
     - **Figure 2**: All 10,000 individual simulation paths

## Methodology

### Geometric Brownian Motion (GBM)

The simulation uses the exponential GBM formula:

```
S(t+Δt) = S(t) × exp((μ - 0.5σ²)Δt + σ√Δt × Z)
```

Where:
- `S(t)` = Stock price at time t
- `μ` = Expected return (drift)
- `σ` = Volatility (standard deviation of log returns)
- `Δt` = Time step (1 day)
- `Z` = Random standard normal variable

### Process Flow

1. **Data Preprocessing**: Load historical data and forward-fill missing values
2. **Log Returns Calculation**: Compute daily log returns from historical prices
3. **Parameter Estimation**: Calculate mean return (μ) and volatility (σ)
4. **Monte Carlo Simulation**: Generate 10,000 price paths using vectorized GBM
5. **Risk Analysis**: Calculate VaR at 95% confidence level
6. **Visualization**: Plot results and compare with actual market data

## Key Outputs

### Metrics Calculated:
- **Average Simulated End Price**: Mean of all simulation endpoints
- **95% VaR**: 5th percentile of return distribution (worst-case scenarios)
- **Standard Deviation Bands**: ±1 SD from mean path
- **Actual vs. Simulated Comparison**: How well the model predicts real prices

### Interpretation:
- **VaR (Red line)**: The price level below which only 5% of simulations fall (95% confidence)
- **Average Path (Green)**: Expected price trajectory
- **SD Bands (Blue)**: One standard deviation range showing typical volatility
- **Actual Price (Purple)**: Real market performance for validation

## 📁 Project Structure

```
Monte-Carlo-Simulation-Stocks/
│
├── Stock_Monte_Sim.py                    # Main simulation script
├── AAPL_GS_MSFT_CAT_5_Year_Close_Price_Data - Static Data.csv
├── README.md                              # This file
└── requirements.txt                       # Python dependencies
```

## 🔍 Example Results

For the period from January 2025 to October 2025:

| Ticker | Starting Price | Avg End Price | 95% VaR Return |
|--------|---------------|---------------|----------------|
| AAPL   | $188.38      | $209.65      | -24.18%         |
| GS     | $470.81      | $506.16      | -27.80%         |
| MSFT   | $359.84      | $393.23      | -27.47%         |
| CAT    | $288.08      | $306.07      | -27.47%         |


## ⚠️ Limitations

- **Independence Assumption**: Stocks are simulated independently; correlations between assets are not modeled
- **Constant Parameters**: Assumes volatility and drift remain constant over the simulation period
- **Normal Distribution**: Assumes returns follow a log-normal distribution (may not capture fat tails)
- **No Market Events**: Does not account for discrete events (earnings, news, crashes)
- **Historical Dependence**: Model quality depends on historical data representativeness

##  Future Enhancements

- [ ] Add correlation matrix for multi-asset portfolio simulation
- [ ] Implement additional models (Jump Diffusion, GARCH)
- [ ] Create interactive dashboard with Plotly
- [ ] Add portfolio optimization features
- [ ] Include transaction costs and dividends
- [ ] Expand to more asset classes (options, bonds)

##  References

- Black, F., & Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities"
- Hull, J. C. (2018). "Options, Futures, and Other Derivatives"
- Jorion, P. (2006). "Value at Risk: The New Benchmark for Managing Financial Risk"

##  License

This project is open source and available under the MIT License.

##  Author

**Jose Marcos O'Carroll**
- GitHub: [@JoseOC042023](https://github.com/JoseOC042023)
- LinkedIn: [Jose](https://www.linkedin.com/in/jose-marcos-o-carroll-871721183/)

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

⭐ If you found this project helpful, please consider giving it a star!
