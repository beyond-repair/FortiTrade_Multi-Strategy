# API Reference

## POST /trading_signal

**Description:**  
Receives market data from TradingView and returns a trade decision based on DeepSeek analysis.

**Request Body (JSON):**
```json
{
  "time": 1680000000000,
  "strategy": "RSI_MeanReversion",
  "signal": "BUY",
  "price": 35000
}

Response:

{
  "signal": "BUY"
}

### **docs/PineScript_Strategy.md**

```markdown
# PineScript Strategy Documentation

The `FortiTrade_Elite.pine` script implements multiple trading strategies with auto selection and risk management. It includes:
- **Scalping:** Based on RSI and Bollinger Bands.
- **Trend Following:** Using EMA crossovers.
- **Trend Reversal:** Combining RSI and MACD.
- **Grid Trading:** Within defined price bounds.
- **Crash Protection:** Exits positions if market drops beyond a set threshold.
- **Turbo Mode:** When live, an external AI decision (DeepSeek) is used for trade execution.