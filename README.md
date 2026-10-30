# 🟠 Copper Stock Analysis 2026

A data analysis project that tracks and compares the 2026 weekly performance of three copper-mining stocks using Python (pandas, matplotlib) and an interactive Power BI dashboard.

## 📌 Overview

Copper is a key industrial metal tied to global growth, electrification and infrastructure demand. This project cleans weekly price data for three copper-related equities, engineers trend and risk indicators, and summarizes which stock delivered the best return for the amount of risk taken.

**Stocks analyzed**

| Ticker | Company | Market |
|---|---|---|
| `FCX` | Freeport-McMoRan | NYSE (USA) |
| `SCCO` | Southern Copper Corporation | NYSE (USA) |
| `HINDCOPPER.NS` | Hindustan Copper Ltd | NSE (India) |

**Period covered:** late December 2025 to October 2026 (weekly data)

## 📂 Repository Structure

```
├── main.py                          # Data cleaning + feature engineering + summary
├── copper_stock_analysis.csv        # Raw weekly OHLCV data
├── copper_clean.csv                 # Cleaned data with calculated indicators
├── copper_summary.csv               # Per-ticker summary statistics
├── dashboard_stock_analysis.pbix    # Power BI dashboard
└── README.md
```

## 🔧 Workflow

1. **Load** the raw weekly OHLCV data.
2. **Inspect** shape, data types, null values and duplicates.
3. **Clean**: parse dates, reorder columns, drop duplicates and missing values, round prices to 2 decimals, sort by ticker and date.
4. **Engineer features** (calculated per ticker):
   - `MA4`: 4-week moving average of the close price
   - `MA10`: 10-week moving average of the close price
   - `Weekly_Return_%`: week-over-week percentage change in close
   - `Volatility_4w`: rolling 4-week standard deviation of weekly returns
5. **Summarize** each ticker: highest price, lowest price, average weekly return, volatility, average volume and total return.
6. **Visualize** the results in Power BI.

## 📊 Data Dictionary

**`copper_clean.csv`**

| Column | Description |
|---|---|
| `Date` | Week start date |
| `Ticker` | Stock symbol |
| `Open`, `High`, `Low`, `Close` | Weekly prices (local currency) |
| `Volume` | Shares traded in the week |
| `MA4`, `MA10` | 4 and 10-week moving averages of close |
| `Weekly_Return_%` | Weekly % change in close |
| `Volatility_4w` | Rolling 4-week std. dev. of weekly returns |

## 📈 Key Results

| Ticker | Highest | Lowest | Avg Weekly Return % | Volatility (weekly std %) | Avg Volume | Total Return % |
|---|---|---|---|---|---|---|
| FCX | 80.07 | 50.45 | 0.71 | 7.83 | 76,174,786 | **+18.53** |
| SCCO | 220.78 | 138.37 | 0.77 | 7.60 | 7,395,143 | **+22.47** |
| HINDCOPPER.NS | 755.97 | 392.30 | -0.59 | 5.06 | 64,638,094 | **-25.96** |

**Takeaways**

- **SCCO** had the best total return (+22.47%) and the highest average weekly return.
- **FCX** also finished positive (+18.53%) but with the highest volatility of the three.
- **HINDCOPPER.NS** was the only decliner (-25.96%), despite having the lowest volatility.

> Prices are in each exchange's local currency (USD for FCX/SCCO, INR for HINDCOPPER.NS), so compare returns and volatility rather than raw price levels.

## 🖥️ Power BI Dashboard

Open `dashboard_stock_analysis.pbix` in [Power BI Desktop](https://powerbi.microsoft.com/desktop/) to explore the interactive dashboard (price trends, moving averages, returns and volatility by ticker).

<!-- Add a screenshot: ![Dashboard](images/dashboard.png) -->

## 🚀 Getting Started

**Requirements:** Python 3.8+, `pandas`, `matplotlib`

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. Install dependencies
pip install pandas matplotlib

# 3. Run the analysis
python main.py
```

> Make sure the raw data filename in `main.py` matches the CSV in your repo (`copper_stock_analysis.csv`).

## 🛠️ Tech Stack

- **Python**: pandas, matplotlib
- **Power BI**: dashboarding and visualization
- **Data**: weekly OHLCV stock data

## 🔮 Future Improvements

- Add price and moving-average charts with matplotlib
- Compare stocks against the copper commodity price (e.g. LME / COMEX)
- Add a correlation matrix across the three tickers
- Calculate risk-adjusted return (Sharpe ratio)
- Automate data download with `yfinance`

## ⚠️ Disclaimer

This project is for educational and analytical purposes only and is not financial advice.

## 📄 License

This project is licensed under the MIT License. Add a `LICENSE` file if you choose to include one.

## 👤 Author

**Your Name**
GitHub: [@shashankyadav9899](https://github.com/shashankyadav9899) · LinkedIn: [shashankyadav9899](https://www.linkedin.com/in/shashank-yadav-574019448/)
