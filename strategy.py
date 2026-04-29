import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from cpz.clients.sync import CPZClient

# Strategy: Net Interest Margin Pairs Trade (Steepening/Flattening)
# Regime 1 (Steepening): Long PNC/FITB, Short GS/STT
# Regime 2 (Flattening): Short PNC/FITB, Long GS/STT

def initialize_client():
    """Initialize CPZ client with environment credentials."""
    strategy_id = os.environ["CPZ_AI_API_STRATEGY_ID"]
    client = CPZClient()
    client.execution.use_broker("alpaca", environment="paper")
    return client, strategy_id

def get_yield_curve_slope(client):
    """Fetch 10Y-2Y Treasury spread from FRED."""
    try:
        # Get 10-year and 2-year Treasury yields
        df_10y = client.data.economic(series_id="DGS10", limit=60)
        df_2y = client.data.economic(series_id="DGS2", limit=60)
        
        if df_10y.empty or df_2y.empty:
            return None, None
        
        # Merge on date
        df = pd.merge(df_10y, df_2y, on='date', suffixes=('_10y', '_2y'))
        df['spread'] = df['value_10y'] - df['value_2y']
        
        # Calculate moving average for smoothing
        df['spread_ma'] = df['spread'].rolling(window=20).mean()
        
        current_spread = df['spread'].iloc[-1]
        ma_spread = df['spread_ma'].iloc[-1]
        
        return current_spread, ma_spread
    except Exception as e:
        print(f"Error fetching yield curve data: {e}")
        return None, None

def determine_regime(current_spread, ma_spread, threshold=0.15):
    """Determine market regime based on yield curve slope.
    
    Args:
        current_spread: Current 10Y-2Y spread
        ma_spread: Moving average of spread
        threshold: Threshold for regime change (in percentage points)
    
    Returns:
        'steepening', 'flattening', or 'neutral'
    """
    if current_spread is None or ma_spread is None:
        return 'neutral'
    
    # Steepening: spread increasing beyond threshold
    if current_spread > ma_spread + threshold:
        return 'steepening'
    # Flattening: spread decreasing beyond threshold
    elif current_spread < ma_spread - threshold:
        return 'flattening'
    else:
        return 'neutral'

def get_current_positions(client):
    """Get current positions to determine if rebalancing is needed."""
    try:
        positions = client.execution.get_positions()
        return {pos.symbol: float(pos.qty) for pos in positions}
    except Exception as e:
        print(f"Error fetching positions: {e}")
        return {}

def execute_regime_trades(client, strategy_id, regime, current_positions, portfolio_value):
    """Execute trades based on regime.
    
    Market-neutral construction: equal notional long and short exposure.
    """
    # Define position sizes (25% per leg for market neutrality)
    position_size = portfolio_value * 0.25
    
    # Define trade legs based on regime
    if regime == 'steepening':
        # Long Asset-Sensitive (Regionals), Short Capital-Light (Fee-based)
        trades = [
            {'symbol': 'PNC', 'side': 'buy', 'notional': position_size},
            {'symbol': 'FITB', 'side': 'buy', 'notional': position_size},
            {'symbol': 'GS', 'side': 'sell', 'notional': position_size},
            {'symbol': 'STT', 'side': 'sell', 'notional': position_size}
        ]
    elif regime == 'flattening':
        # Short Asset-Sensitive (Regionals), Long Capital-Light (Fee-based)
        trades = [
            {'symbol': 'PNC', 'side': 'sell', 'notional': position_size},
            {'symbol': 'FITB', 'side': 'sell', 'notional': position_size},
            {'symbol': 'GS', 'side': 'buy', 'notional': position_size},
            {'symbol': 'STT', 'side': 'buy', 'notional': position_size}
        ]
    else:
        # Neutral: close all positions
        trades = []
        for symbol in ['PNC', 'FITB', 'GS', 'STT']:
            if symbol in current_positions and current_positions[symbol] != 0:
                qty = abs(current_positions[symbol])
                side = 'sell' if current_positions[symbol] > 0 else 'buy'
                trades.append({'symbol': symbol, 'side': side, 'qty': qty})
    
    # Execute trades
    for trade in trades:
        try:
            if 'notional' in trade:
                # Calculate quantity from notional
                try:
                    quotes = client.data.quotes([trade['symbol']])
                    if quotes and len(quotes) > 0:
                        quote = quotes[0]
                        price = quote.ask_price if trade['side'] == 'buy' else quote.bid_price
                        if price and price > 0:
                            qty = int(trade['notional'] / price)
                        else:
                            print(f"Invalid price for {trade['symbol']}, skipping")
                            continue
                    else:
                        print(f"No quote data for {trade['symbol']}, skipping")
                        continue
                except Exception as e:
                    print(f"Error fetching quote for {trade['symbol']}: {e}")
                    continue
            else:
                qty = trade['qty']
            
            if qty > 0:
                order = client.execution.order(
                    symbol=trade['symbol'],
                    qty=qty,
                    side=trade['side'],
                    order_type='market',
                    time_in_force='day',
                    strategy_id=strategy_id
                )
                print(f"Executed: {trade['side'].upper()} {qty} {trade['symbol']}")
        except Exception as e:
            print(f"Error executing trade for {trade['symbol']}: {e}")

def generate_signals():
    """Main strategy execution function."""
    client, strategy_id = initialize_client()
    
    # Get portfolio value
    try:
        account = client.execution.get_account()
        portfolio_value = float(account.portfolio_value)
    
    # Get yield curve data and determine regime
=======
=======
    
    # Get yield curve data and determine regime
    current_spread, ma_spread = get_yield_curve_slope(client)
    regime = determine_regime(current_spread, ma_spread)
    
    print(f"Current Spread: {current_spread:.2f}%, MA Spread: {ma_spread:.2f}%")
    print(f"Regime: {regime.upper()}")
    
    # Get current positions
    current_positions = get_current_positions(client)
    
    # Execute trades based on regime
    execute_regime_trades(client, strategy_id, regime, current_positions, portfolio_value)
    
    # Return signal weights for tracking (market-neutral)
    if regime == 'steepening':
        return {'PNC': 0.25, 'FITB': 0.25, 'GS': -0.25, 'STT': -0.25}
    elif regime == 'flattening':
        return {'PNC': -0.25, 'FITB': -0.25, 'GS': 0.25, 'STT': 0.25}
    else:
        return {'PNC': 0, 'FITB': 0, 'GS': 0, 'STT': 0}

if __name__ == '__main__':
    signals = generate_signals()
    print(f"Signal Weights: {signals}")