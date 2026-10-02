#!/usr/bin/env python3
"""backtest.py — CSV backtest using the Claim-0 rule decision engine."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from fortitrade.csv_io import load_market_csv
from fortitrade.decision import get_trade_decision

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "data" / "historical_data.csv"


def backtest(data: list[dict]) -> list[dict]:
    results = []
    for entry in data:
        decision = get_trade_decision(entry)
        row = dict(entry)
        row["ai_decision"] = decision
        results.append(row)
        print(
            f"Time: {entry['time']}, Price: {entry['price']}, AI Decision: {decision}"
        )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="FortiTrade CSV backtest (Claim-0)")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument(
        "--out",
        type=Path,
        default=REPO_ROOT / "data" / "backtest_results.json",
    )
    args = parser.parse_args(argv)
    if not args.csv.is_file():
        print(f"CSV not found: {args.csv}", file=sys.stderr)
        return 1
    results = backtest(load_market_csv(args.csv))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"wrote {args.out} ({len(results)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
