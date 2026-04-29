<p align="left">
  <a href="https://ai.cpz-lab.com/">
    <img src="https://drive.google.com/uc?id=1JY-PoPj9GHmpq3bZLC7WyJLbGuT1L3hN" alt="CPZ Lab" width="150">
  </a>
</p>

# Steepening (1)

> *Generated with [CPZAI](https://ai.cpz-lab.com/)*

A pairs_trading, profitability_factor, global_macro, regime_switching trading strategy built on CPZAI Platform.

## Strategy Overview

**Type:** Pairs_trading, profitability_factor, global_macro, regime_switching

Systematic Pairs Trade based on Net Interest Margin divergence between traditional commercial lenders and fee-based financial institutions. Regime-switching logic triggered by yield curve slope (10Y-2Y spread). Long Regionals/Short Capital Markets when curve steepens, reverse when it flattens. Market-neutral construction isolates the curve factor.

## Quick Start

```bash
# Clone repository
git clone https://github.com/thearcaneaberration-glitch/strategy-steepening-1.git
cd strategy-steepening-1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -e .

# Run backtest
python backtest.py

# Run live strategy (requires CPZ credentials)
python strategy.py
```

## Configuration

Create a `.env` file with your credentials:

| Variable | Description |
|----------|-------------|
| `CPZ_AI_API_KEY` | CPZAI API key |
| `CPZ_AI_API_SECRET_KEY` | CPZAI secret key |
| `CPZ_AI_API_STRATEGY_ID` | Your strategy ID |
| `CPZ_BROKER` | Broker (default: alpaca) |
| `CPZ_BROKER_ENVIRONMENT` | paper or live |

> **Note:** When running on CPZ Platform, credentials are automatically injected.

## Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Project metadata, dependencies, ruff config |
| `strategy.py` | Main strategy with signal generation + CPZ execution |
| `backtest.py` | Backtrader backtesting framework with metrics |
| `tests/test_strategy.py` | Signal interface validation (pytest) |
| `METHODOLOGY.md` | Detailed strategy methodology & research |
| `.env.example` | Credential template (copy to .env) |

## Architecture

```
strategy.py                    backtest.py
    │                              │
    ├── generate_signals()  ◄──────┤ imports from strategy
    ├── initialize_client()        │
    └── run_strategy()             └── StrategyWrapper (Backtrader)
         │
         ▼
    CPZAI Platform
         │
         ▼
    Broker (Alpaca, etc.)
```

## Usage Examples

### Run Backtest

```python
python backtest.py
```

Outputs comprehensive metrics including:
- Total Return & Annualized Return
- Sharpe Ratio & Volatility
- Maximum Drawdown
- Win Rate & Trade Statistics
- Alpha vs SPY Benchmark

### Run Live Strategy

```python
# Ensure .env is configured
python strategy.py
```

### Import in Custom Scripts

```python
from strategy import generate_signals, SYMBOLS

# Get signals for current data
data = load_your_data()  # Dict of {symbol: DataFrame}
signals = generate_signals(data, state={})
print(signals)  # {'SPY': 0.5, 'QQQ': 0.3, ...}
```

## Dependencies

Defined in `pyproject.toml`. Key packages:

- `cpz-ai` - Order execution via CPZ Platform
- `backtrader` - Backtesting framework
- `yfinance` - Market data
- `pandas` / `numpy` - Data processing
- `python-dotenv` - Environment configuration

## Strategy Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for detailed strategy documentation including:
- Research hypothesis
- Theoretical framework
- Signal generation logic
- Risk management approach
- Performance expectations

## License

This project is licensed under the MIT License.

---

*Built with [CPZAI Platform](https://ai.cpz-lab.com/)*