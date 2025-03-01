from fastapi import FastAPI, Request
import uvicorn
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = FastAPI(title="Local Trading AI Webhook with DeepSeek")

# Load the quantized DeepSeek-R1 model (4-bit version)
model_name = "bartowski/DeepSeek-R1-GGUF"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
# For GPU use device=0; for CPU use device=-1 (CPU inference may be slow)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

def get_trade_decision(data: dict) -> str:
    """
    Construct a prompt using market data, trade signals, and additional inputs,
    then generate a decision (BUY, SELL, or HOLD) using DeepSeek.
    
    (Note: Further enhancements like ensemble models or meta reinforcement learning
    can be integrated here for an extra competitive edge.)
    """
    prompt = (
        f"Market data and signals: {data}. "
        "Based on this information, what is the optimal trade decision? "
        "Respond with only BUY, SELL, or HOLD."
    )
    
    output = generator(prompt, max_new_tokens=10, temperature=0.2)
    generated_text = output[0]['generated_text'].strip().upper()
    
    if "BUY" in generated_text:
        decision = "BUY"
    elif "SELL" in generated_text:
        decision = "SELL"
    else:
        decision = "HOLD"
    return decision

@app.post("/trading_signal")
async def trading_signal(request: Request):
    data = await request.json()
    print("Received data:", data)
    
    decision = get_trade_decision(data)
    print("Trade decision:", decision)
    return {"signal": decision}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)