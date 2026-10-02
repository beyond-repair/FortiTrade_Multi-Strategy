# API Reference

## GET /health

Returns `{"status": "ok", "engine": "rules"}`.

## POST /trading_signal

Receives market JSON (typically from a TradingView alert experiment) and returns a trade decision from the Claim-0 rule engine.

**Request body (JSON):**

```json
{
  "time": "2024-01-02T09:30:00Z",
  "strategy": "RSI_MeanReversion",
  "signal": "BUY",
  "price": 35000,
  "rsi": 28.5
}
```

**Response:**

```json
{
  "signal": "BUY"
}
```

`signal` is always one of `BUY`, `SELL`, `HOLD`.
