#!/usr/bin/env python
"""
live_trading.py

This script simulates a live trading session by reading live market data from a CSV file,
processing each entry with the local DeepSeek AI decision engine, and printing the decisions.
In a real-world scenario, these decisions would be sent to your order execution system (e.g., via 3Commas).
"""

import time
import csv
from src.local_app import get_trade_decision

def load_live_data(file_path):
    """
    Load live market data from a CSV file.
    Expected CSV format: time,price,rsi,signal
    """
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "time": row["time"],
                "price": float(row["price"]),
                "rsi": float(row["rsi"]),
                "signal": row["signal"]
            })
    return data

def simulate_live_trading(data_stream):
    """
    Simulate a live trading session by processing each data point with a delay.
    """
    for data in data_stream:
        decision = get_trade_decision(data)
        print(f"Live Time: {data['time']}, Price: {data['price']}, AI Decision: {decision}")
        # In a production environment, trigger order execution here (e.g., via webhook/API call).
        time.sleep(1)  # Simulate delay between market bars

if __name__ == "__main__":
    # Path to your live market data CSV file
    file_path = "live_data.csv"
    live_data = load_live_data(file_path)
    simulate_live_trading(live_data)