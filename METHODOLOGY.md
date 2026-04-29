<h1 align="center">Steepening (1)</h1>
<h3 align="center">Systematic Trading Strategy Methodology</h3>

<p align="center">
  <strong>Classification:</strong> Proprietary | <strong>Version:</strong> 1.0 | <strong>Date:</strong> April 29, 2026
</p>

---

## 1. Executive Summary

> *A concise overview of the strategy's core thesis, target markets, and expected edge.*

| Attribute | Value |
|-----------|-------|
| **Strategy Type** | Pairs Trading, Profitability Factor, Global Macro, Regime Switching |
| **Asset Class** | *e.g., Equities, Futures, Crypto* |
| **Time Horizon** | *e.g., Intraday, Swing, Long-term* |
| **Target Sharpe** | *e.g., 1.5 - 2.5* |
| **Max Drawdown** | *e.g., < 15%* |

---

## 2. Research Hypothesis

### 2.1 Market Inefficiency

*Describe the specific market inefficiency or behavioral bias being exploited...*

### 2.2 Theoretical Foundation

*Explain the academic or empirical basis for the hypothesis...*

### 2.3 Edge Persistence

*Why do you believe this edge will persist? What structural factors support it?*

---

## 3. Signal Generation

### 3.1 Primary Indicators

| Indicator | Parameters | Signal Logic |
|-----------|------------|--------------|
| *e.g., RSI* | *Period: 14* | *Long < 30, Short > 70* |
| *e.g., SMA Cross* | *Fast: 20, Slow: 50* | *Long on golden cross* |

### 3.2 Entry Conditions

```
IF [primary_signal] AND [confirmation_filter] AND [regime_filter]:
    ENTER position with [sizing_logic]
```

### 3.3 Exit Conditions

- **Take Profit:** *Define profit target logic...*
- **Stop Loss:** *Define stop loss logic...*
- **Time-based Exit:** *Define time-based exit rules...*

---

## 4. Risk Management

### 4.1 Position Sizing

*Describe the position sizing methodology (e.g., Kelly Criterion, Fixed Fractional, Volatility-based)...*

### 4.2 Portfolio Constraints

| Constraint | Limit |
|------------|-------|
| Max Position Size | *e.g., 5% of NAV* |
| Max Sector Exposure | *e.g., 20% of NAV* |
| Max Correlation | *e.g., 0.6 between positions* |
| Max Leverage | *e.g., 2x* |

### 4.3 Drawdown Controls

*Describe circuit breakers and drawdown management protocols...*

---

## 5. Performance Expectations

### 5.1 Expected Characteristics

| Metric | Target | Acceptable Range |
|--------|--------|------------------|
| Annual Return | *e.g., 25%* | *15% - 40%* |
| Sharpe Ratio | *e.g., 2.0* | *1.5 - 3.0* |
| Max Drawdown | *e.g., 10%* | *< 20%* |
| Win Rate | *e.g., 55%* | *50% - 65%* |
| Profit Factor | *e.g., 1.8* | *> 1.5* |

### 5.2 Regime Analysis

*How does the strategy perform across different market regimes?*

---

## 6. Implementation

### 6.1 Data Requirements

| Data Type | Source | Frequency |
|-----------|--------|-----------|
| *e.g., OHLCV* | *e.g., Polygon* | *1-minute* |
| *e.g., Fundamentals* | *e.g., SEC EDGAR* | *Daily* |

### 6.2 Execution Considerations

*Describe slippage assumptions, order types, and execution timing...*

### 6.3 Technology Stack

*Describe the technical infrastructure and dependencies...*

---

## 7. Monitoring & Review

### 7.1 Key Metrics to Monitor

- Realized vs. Expected Sharpe
- Drawdown trajectory
- Win rate stability
- Correlation to benchmarks

### 7.2 Review Schedule

| Review Type | Frequency |
|-------------|-----------|
| Performance Review | Weekly |
| Risk Assessment | Monthly |
| Strategy Review | Quarterly |
| Full Audit | Annually |

---

<p align="center">
  <sub>
    <strong>Disclaimer:</strong> This document is for informational purposes only and does not constitute investment advice.
    Past performance is not indicative of future results. Trading involves substantial risk of loss.
  </sub>
</p>

<p align="center">
  <sub>Built with <a href="https://ai.cpz-lab.com/">CPZAI Platform</a> — The AI-Native Systematic Trading Operating System</sub>
</p>