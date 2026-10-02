"""Tests for deterministic rule decision engine."""

from fortitrade.decision import get_trade_decision, rule_based_decision


def test_rsi_oversold_buys():
    assert rule_based_decision({"rsi": 25, "signal": "HOLD", "price": 100}) == "BUY"


def test_rsi_overbought_sells():
    assert rule_based_decision({"rsi": 75, "signal": "HOLD", "price": 100}) == "SELL"


def test_signal_confirmed_by_rsi():
    assert rule_based_decision({"rsi": 40, "signal": "BUY", "price": 100}) == "BUY"
    assert rule_based_decision({"rsi": 60, "signal": "SELL", "price": 100}) == "SELL"


def test_plain_signal_when_rsi_neutral():
    assert rule_based_decision({"rsi": 50, "signal": "BUY", "price": 100}) == "BUY"
    assert rule_based_decision({"rsi": 50, "signal": "HOLD", "price": 100}) == "HOLD"


def test_missing_fields_hold():
    assert get_trade_decision({}) == "HOLD"
    assert get_trade_decision(None) == "HOLD"


def test_string_rsi_coercion():
    assert get_trade_decision({"rsi": "22.5", "signal": "HOLD"}) == "BUY"
