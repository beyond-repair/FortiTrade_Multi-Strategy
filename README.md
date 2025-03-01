# FortiTrade Multi-Strategy

FortiTrade Multi-Strategy is a plug-and-play, integrated trading system that combines advanced multi-strategy TradingView Pine Script with a local AI decision engine powered by a quantized DeepSeek model. The solution is designed for rapid, real-time trade decision-making and supports seamless integration with platforms like 3Commas for live order execution.

## Features
- **Multiple Trading Strategies:** Scalping, Trend Following, Trend Reversal, and Grid Trading with automated risk management and crash protection.
- **Auto Strategy Selection:** Dynamically chooses the best strategy based on real-time market conditions.
- **Turbo Mode Integration:** When live mode is enabled, an external AI decision (via DeepSeek) overrides the auto signals for high-confidence trades.
- **Local AI Processing:** Uses a 4-bit quantized version of DeepSeek-R1 for efficient inference on local hardware.
- **No-Code Integration:** Works out-of-the-box with TradingView alerts and webhook setups (e.g., via 3Commas) for live trading.

## Quick Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/FortiTrade-Multi-Strategy.git
   cd FortiTrade-Multi-Strategy

2. Deploy the Pine Script:

Open TradingView, create a new script, and paste the content of pinescript/FortiTrade_Elite.pine.

Configure alerts to send webhook data to your local AI server (e.g., http://localhost:8000/trading_signal).



3. Run the Local AI Server:

Navigate to the src/ folder.

Install dependencies:

pip install -r requirements.txt

Start the FastAPI service:

python local_app.py



4. Integrate with 3Commas (Optional):

Set up 3Commas to receive alerts from TradingView and execute orders on your exchange (e.g., Kraken).




Documentation

Please refer to the files in the docs/ folder for detailed instructions on installation, configuration, API reference, and strategy logic.
