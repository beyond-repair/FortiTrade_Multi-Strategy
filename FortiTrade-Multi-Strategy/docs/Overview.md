# Overview

FortiTrade Multi-Strategy is an integrated trading system that combines advanced multi-strategy logic on TradingView with a local AI decision engine powered by a quantized DeepSeek model. The system is designed for rapid, real-time trade decision-making and supports both paper trading (sandbox mode) and live trading. It features:

- **Multiple Trading Strategies:**  
  Scalping, Trend Following, Trend Reversal, and Grid Trading with automated risk management and crash protection.

- **Auto Strategy Selection:**  
  Dynamically selects the optimal strategy based on current market conditions.

- **Turbo Mode Integration:**  
  In live mode, an external AI decision—provided by the DeepSeek-based FastAPI service—overrides auto-generated signals for high-confidence trade execution.

- **Local AI Processing:**  
  Utilizes a 4-bit quantized version of DeepSeek-R1 for efficient, real-time inference on local hardware.

- **Seamless Integration:**  
  Works with TradingView alerts (via webhooks) and can integrate with platforms like 3Commas for live order execution on exchanges (e.g., Kraken).

- **Backtesting & Live Trading Support:**  
  Includes scripts for backtesting historical data as well as a live trading simulation to validate the system before deployment.

This repository contains:
- A sophisticated TradingView Pine Script (`pinescript/FortiTrade_Elite.pine`) that implements the multi-strategy logic.
- A local FastAPI service (`src/local_app.py`) for AI decision-making using DeepSeek.
- Utility scripts for backtesting (`scripts/backtest.py`) and live trading simulation (`scripts/live_trading.py`).
- Detailed documentation for installation, configuration, API reference, and strategy logic.

FortiTrade Multi-Strategy is a plug-and-play, no-code solution designed for both novice and experienced traders, enabling adaptive trading in volatile markets.