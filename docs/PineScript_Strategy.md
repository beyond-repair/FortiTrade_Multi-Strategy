# PineScript Strategy Documentation

`pinescript/FortiTrade_Elite.pine` (`//@version=6`) implements multiple strategies with auto selection and risk inputs:

- **Scalping:** RSI and Bollinger Bands
- **Trend Following:** EMA crossovers
- **Trend Reversal:** RSI and MACD
- **Grid Trading:** within configured price bounds
- **Crash Protection:** exit when drop exceeds threshold
- **Webhook input:** `mlWebhookURL` defaults to `http://localhost:8000/trading_signal`

Pine runs on TradingView. The local Python webhook is a separate Claim-0 sketch and does not execute exchange orders.
