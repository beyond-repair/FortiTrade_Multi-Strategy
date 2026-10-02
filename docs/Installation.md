# Installation Guide

## Prerequisites

- Python 3.10+
- Optional: TradingView account (for Pine paste only)

No GPU and no Hugging Face model download are required for the Claim-0 default path.

## Steps

```bash
git clone https://github.com/beyond-repair/FortiTrade_Multi-Strategy.git
cd FortiTrade_Multi-Strategy
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python main.py
pytest -q
```

### FastAPI webhook

```bash
python -m fortitrade serve
```

### Pine Script

Paste `pinescript/FortiTrade_Elite.pine` into TradingView. For experiments only, set the webhook URL to `http://localhost:8000/trading_signal` (sandbox).

### Configuration

- Default decision engine: rules (`FORTITRADE_ENGINE` unset or `rules`).
- Sample CSVs: `data/historical_data.csv`, `data/live_data.csv`.
