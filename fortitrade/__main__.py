"""python -m fortitrade — demo entry (backtest sample CSV + optional serve)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from fortitrade.csv_io import load_market_csv
from fortitrade.decision import get_trade_decision


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "data" / "historical_data.csv"


def run_backtest(csv_path: Path) -> list[dict]:
    data = load_market_csv(csv_path)
    results = []
    for entry in data:
        decision = get_trade_decision(entry)
        out = dict(entry)
        out["ai_decision"] = decision
        results.append(out)
        print(
            f"Time: {entry['time']}, Price: {entry['price']}, "
            f"RSI: {entry['rsi']}, TV: {entry['signal']}, Decision: {decision}"
        )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="FortiTrade Multi-Strategy Claim-0 demo (rules engine)"
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="demo",
        choices=["demo", "backtest", "serve"],
        help="demo/backtest: run CSV decisions; serve: uvicorn webhook",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help="Path to market CSV (default: data/historical_data.csv)",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional JSON path for backtest results",
    )
    args = parser.parse_args(argv)

    if args.command in ("demo", "backtest"):
        if not args.csv.is_file():
            print(f"CSV not found: {args.csv}", file=sys.stderr)
            return 1
        print("--- FortiTrade Claim-0 demo (rule engine) ---")
        results = run_backtest(args.csv)
        print(f"rows={len(results)}")
        if args.out:
            args.out.write_text(json.dumps(results, indent=2), encoding="utf-8")
            print(f"wrote {args.out}")
        return 0

    # serve
    import uvicorn

    from fortitrade.app import app

    uvicorn.run(app, host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
