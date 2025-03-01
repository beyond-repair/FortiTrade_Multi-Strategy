# Installation Guide

## Prerequisites
- TradingView account
- Python 3.8+
- Required Python packages (see `requirements.txt`)
- A capable GPU (recommended) or CPU for local AI inference

## Steps
1. Clone the repository.
2. Deploy the Pine Script to TradingView.
3. Configure TradingView alerts with your webhook URL.
4. Install Python dependencies:
   ```bash
   pip install -r src/requirements.txt

5. Run the FastAPI service:

python src/local_app.py


6. (Optional) Integrate with 3Commas.



### **docs/Configuration.md**

```markdown
# Configuration

## TradingView Pine Script
- **Sandbox Mode:** Toggle between simulation (`true`) and live trading (`false`).
- **Webhook URL:** Set the `mlWebhookURL` input to your local FastAPI endpoint (e.g., `http://localhost:8000/trading_signal`).
- **External Signal:** This input is updated via webhook responses to execute trades in live mode.

## FastAPI Service
- **Model:** The service uses a quantized version of DeepSeek-R1 from Hugging Face (e.g., "bartowski/DeepSeek-R1-GGUF").
- **Device Setting:** Adjust the `device` parameter in `pipeline(...)` for GPU (device=0) or CPU (device=-1).