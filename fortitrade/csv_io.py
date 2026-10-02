"""CSV loaders for backtest / live simulation (time,price,rsi,signal)."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


def load_market_csv(file_path: str | Path) -> list[dict[str, Any]]:
    path = Path(file_path)
    rows: list[dict[str, Any]] = []
    with path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        required = {"time", "price", "rsi", "signal"}
        if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"CSV {path} must have columns time,price,rsi,signal; "
                f"got {reader.fieldnames!r}"
            )
        for row in reader:
            rows.append(
                {
                    "time": row["time"],
                    "price": float(row["price"]),
                    "rsi": float(row["rsi"]),
                    "signal": row["signal"],
                }
            )
    return rows
