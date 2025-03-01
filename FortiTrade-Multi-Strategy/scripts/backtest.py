#!/usr/bin/env python
"""
backtest.py

This script performs backtesting on historical market data using the local DeepSeek AI decision engine.
It loads historical data from a CSV file, simulates trade decisions, and outputs the results.
"""

import csv
import json
from src.local_app import get_trade_decision

def load_historical_data(file_path):
    """
    Load historical market data from a CSV file.
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

def backtest(data):
    """
    Simulate AI decision-making on the historical data.
    """
    results = []
    for entry in data:
        decision = get_trade_decision(entry)
        entry["ai_decision"] = decision
        results.append(entry)
        print(f"Time: {entry['time']}, Price: {entry['price']}, AI Decision: {decision}")
    return results

if __name__ == "__main__":
    # Path to your historical data CSV file
    file_path = "historical_data.csv"
    data = load_historical_data(file_path)
    backtest_results = backtest(data)
    # Optionally, save backtest results to a JSON file for further analysis
    with open("backtest_results.json", "w") as outfile:
        json.dump(backtest_results, outfile, indent=4)