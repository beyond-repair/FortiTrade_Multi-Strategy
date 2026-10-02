# Overview

FortiTrade Multi-Strategy is an archive-queue **Claim-0** sketch that pairs a TradingView Pine multi-strategy script with a local FastAPI decision webhook.

## Components

- **Pine Script** (`pinescript/FortiTrade_Elite.pine`): scalping, trend following, trend reversal, grid trading, crash protection, and webhook URL input for an external signal.
- **Local webhook** (`fortitrade/app.py`): `POST /trading_signal` returns `{"signal": "BUY"|"SELL"|"HOLD"}` using a deterministic RSI/signal rule engine (no GPU, no model download).
- **CSV sims** (`scripts/backtest.py`, `scripts/live_trading.py`): offline validation against sample CSVs in `data/`.

## Honest scope

This is **not** a live trading product. The original DeepSeek-GGUF transformers load was removed because it cannot work as written. Optional `FORTITRADE_ENGINE=transformers` is reserved and still falls back to rules.
