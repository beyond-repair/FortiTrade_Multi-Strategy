"""CSV backtest / live simulation path tests."""

from pathlib import Path

from fortitrade.csv_io import load_market_csv
from fortitrade.decision import get_trade_decision

# scripts/ is on pytest pythonpath
from backtest import backtest, main as backtest_main
from live_trading import simulate_live_trading, main as live_main

REPO = Path(__file__).resolve().parent.parent
HIST = REPO / "data" / "historical_data.csv"
LIVE = REPO / "data" / "live_data.csv"


def test_load_historical_csv():
    rows = load_market_csv(HIST)
    assert len(rows) >= 4
    assert set(rows[0]) >= {"time", "price", "rsi", "signal"}


def test_backtest_assigns_decisions():
    rows = load_market_csv(HIST)
    results = backtest(rows)
    assert len(results) == len(rows)
    assert all(r["ai_decision"] in {"BUY", "SELL", "HOLD"} for r in results)
    # First sample row has rsi 28.5 → BUY
    assert results[0]["ai_decision"] == "BUY"


def test_backtest_cli(tmp_path):
    out = tmp_path / "results.json"
    assert backtest_main(["--csv", str(HIST), "--out", str(out)]) == 0
    assert out.is_file()


def test_live_simulation_no_delay():
    rows = load_market_csv(LIVE)
    decisions = simulate_live_trading(rows, delay=0.0)
    assert len(decisions) == len(rows)
    assert all(d in {"BUY", "SELL", "HOLD"} for d in decisions)


def test_live_cli():
    assert live_main(["--csv", str(LIVE), "--delay", "0"]) == 0


def test_legacy_src_import():
    from src.local_app import get_trade_decision as legacy

    assert legacy({"rsi": 10, "signal": "HOLD"}) == "BUY"


def test_get_trade_decision_matches_engine():
    row = load_market_csv(HIST)[0]
    assert get_trade_decision(row) in {"BUY", "SELL", "HOLD"}
