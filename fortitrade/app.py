"""FastAPI webhook — POST /trading_signal → {"signal": BUY|SELL|HOLD}."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request

from fortitrade.decision import get_trade_decision

app = FastAPI(
    title="FortiTrade Local Decision Webhook",
    description=(
        "Claim-0 sketch: deterministic offline BUY/SELL/HOLD decisions for "
        "TradingView webhook payloads. Not a live trading desk."
    ),
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "engine": "rules"}


@app.post("/trading_signal")
async def trading_signal(request: Request) -> dict[str, str]:
    data: Any = await request.json()
    if not isinstance(data, dict):
        data = {"raw": data}
    decision = get_trade_decision(data)
    return {"signal": decision}


def create_app() -> FastAPI:
    return app
