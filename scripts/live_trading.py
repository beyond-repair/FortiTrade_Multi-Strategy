#!/usr/bin/env python3
"""live_trading.py — simulate a live stream from CSV (no exchange orders)."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from fortitrade.csv_io import load_market_csv
from fortitrade.decision import get_trade_decision

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "data" / "live_data.csv"


def simulate_live_trading(data_stream: list[dict], delay: float = 0.0) -> list[str]:
    decisions: list[str] = []
    for data in data_stream:
        decision = get_trade_decision(data)
        decisions.append(decision)
        print(
            f"Live Time: {data['time']}, Price: {data['price']}, AI Decision: {decision}"
        )
        if delay > 0:
            time.sleep(delay)
    return decisions


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="FortiTrade live CSV simulation (Claim-0; no orders)"
    )
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds between bars (default 0 for tests/demo)",
    )
    args = parser.parse_args(argv)
    if not args.csv.is_file():
        print(f"CSV not found: {args.csv}", file=sys.stderr)
        return 1
    simulate_live_trading(load_market_csv(args.csv), delay=args.delay)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
