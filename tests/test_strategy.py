"""Validate strategy interface contract."""
import pandas as pd
from strategy import generate_signals, SYMBOLS


def test_symbols_defined():
    """SYMBOLS must be a non-empty list of ticker strings."""
    assert isinstance(SYMBOLS, list) and len(SYMBOLS) > 0
    assert all(isinstance(s, str) for s in SYMBOLS)


def test_generate_signals_returns_weights():
    """generate_signals must return a dict of symbol -> float weights."""
    dummy_data = {
        s: pd.DataFrame({
            "open": [100.0], "high": [101.0], "low": [99.0],
            "close": [100.5], "volume": [1000000],
        })
        for s in SYMBOLS
    }
    result = generate_signals(dummy_data, {})
    assert isinstance(result, dict), f"Expected dict, got {type(result)}"
    for symbol, weight in result.items():
        assert isinstance(weight, (int, float)), f"{symbol} weight must be numeric"
        assert -1.0 <= weight <= 1.0, f"{symbol} weight {weight} outside [-1, 1]"
