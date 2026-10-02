"""Deterministic offline trade decision engine (Claim-0).

Replaces the broken DeepSeek-GGUF / transformers load. Default path needs
no GPU and no model download. Optional env FORTITRADE_ENGINE=transformers
is reserved for a future optional path and currently falls back to rules.
"""

from __future__ import annotations

import os
from typing import Any, Mapping


VALID_SIGNALS = frozenset({"BUY", "SELL", "HOLD"})


def _as_float(value: Any, default: float | None = None) -> float | None:
    if value is None:
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _normalize_signal(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip().upper()
    if text in VALID_SIGNALS:
        return text
    return None


def rule_based_decision(data: Mapping[str, Any]) -> str:
    """Heuristic BUY/SELL/HOLD from rsi / signal / price fields.

    Priority:
    1. Strong RSI extremes (oversold < 30 → BUY, overbought > 70 → SELL)
    2. Incoming TV signal confirmed by RSI band (BUY & rsi < 45, SELL & rsi > 55)
    3. Incoming TV signal alone if present
    4. HOLD
    """
    rsi = _as_float(data.get("rsi"))
    incoming = _normalize_signal(data.get("signal"))

    if rsi is not None:
        if rsi < 30:
            return "BUY"
        if rsi > 70:
            return "SELL"
        if incoming == "BUY" and rsi < 45:
            return "BUY"
        if incoming == "SELL" and rsi > 55:
            return "SELL"

    if incoming in ("BUY", "SELL", "HOLD"):
        return incoming

    return "HOLD"


def get_trade_decision(data: Mapping[str, Any] | None) -> str:
    """Public decision API used by FastAPI and CSV scripts.

    Default engine is deterministic rules. Setting FORTITRADE_ENGINE=transformers
    currently still uses rules (transformers path is a stub hook only).
    """
    payload: Mapping[str, Any] = data or {}
    engine = os.environ.get("FORTITRADE_ENGINE", "rules").strip().lower()
    if engine == "transformers":
        # Reserved: optional offline/online LLM path. Claim-0 default must not
        # download multi-GB weights or require GPU, so fall back to rules.
        return rule_based_decision(payload)
    return rule_based_decision(payload)
