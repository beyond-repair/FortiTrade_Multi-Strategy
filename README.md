<div align="center">

```
╔════════════════════════════════════════════════════════════╗
║   ATOMIC DREAM LABS  ·  BEYOND-REPAIR                        ║
╚════════════════════════════════════════════════════════════╝
```

# FortiTrade Multi-Strategy

### TradingView Pine + local decision webhook sketch. Not a live desk.

[![Lifecycle](https://img.shields.io/badge/●_ARCHIVE-64748b?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_0-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   ARCHIVE QUEUE (Claim-0 runnable sketch)
CLAIM       0
NOT CLAIMED profit · live trading · product
```

</div>

---

> **ARCHIVE QUEUE.** Historical sketch repaired to Claim-0 runnable. No profit, deployment, or product claim.

## CI

Sweep-280 added `.github/workflows/pytest.yml`. Local `pytest -q` on pre-CI head `49af08530a020150606173adcd8612e0ba2446cc` passed 19 tests. A remote Actions conclusion is not claimed until a run on the CI commit is observed. Green CI is not a profit, live-order, or product claim.

## Status

**RUNNABLE SKETCH — NOT A COMPLETE PRODUCT.**

A stranger can clone, install, run the demo / FastAPI webhook, and pass pytest. This does **not** place live orders, guarantee profit, or ship a trading product.

Archive-queue under [ADL-Governance](https://github.com/beyond-repair/ADL-Governance).

## What works (Claim-0)

| Surface | Behavior |
| --- | --- |
| `python main.py` / `python -m fortitrade` | CSV backtest demo with deterministic rule engine |
| `POST /trading_signal` | FastAPI webhook → `{"signal": "BUY"\|"SELL"\|"HOLD"}` |
| `scripts/backtest.py` / `scripts/live_trading.py` | Sample CSV simulation (no exchange) |
| `pinescript/FortiTrade_Elite.pine` | TradingView paste (`//@version=6`) |
| `pytest` | Decision rules + TestClient webhook + CSV paths |

**Decision engine:** default path is offline RSI/signal heuristics. The original DeepSeek-GGUF / `transformers` load was broken (GGUF ≠ CausalLM; GPU + multi-GB download). Optional env `FORTITRADE_ENGINE=transformers` is a reserved stub and still uses rules.

## Quick start

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

Serve the webhook (optional):

```bash
python -m fortitrade serve
# or: uvicorn fortitrade.app:app --host 127.0.0.1 --port 8000
# curl -X POST http://127.0.0.1:8000/trading_signal \
#   -H 'content-type: application/json' \
#   -d '{"time":"t","price":35000,"rsi":28,"signal":"BUY"}'
```

Pine Script: open TradingView → paste `pinescript/FortiTrade_Elite.pine`. Point alerts at `http://localhost:8000/trading_signal` only in sandbox experiments.

## Layout

```
├── fortitrade/          ← installable package (decision + FastAPI)
├── src/local_app.py     ← legacy import shim
├── scripts/             ← backtest + live CSV sims
├── data/                ← sample historical_data.csv / live_data.csv
├── pinescript/          ← FortiTrade_Elite.pine (identity preserved)
├── docs/                ← installation / API / overview
├── tests/
├── main.py
└── requirements.txt
```

## What this repository is not

- Not a profitable strategy, live desk, or 3Commas production integration.
- Not a verified DeepSeek / LLM inference stack.
- Not financial advice. Do not use for live capital.

Governance: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance).

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

**William (Brian) Ware** · [Atomic Dream Labs](https://github.com/beyond-repair)  
Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
