# CLAIM_STATUS

**Repository:** FortiTrade_Multi-Strategy
**Classification:** ARCHIVED
**Claim Level:** 0
**Status:** ARCHIVE QUEUE
**Last Verified:** 2026-11-23

## Summary
Historical TradingView Pine + local decision webhook sketch. Claim-0 runnable (CSV backtest demo, FastAPI webhook, pytest CI green). Not a live trading product, no profit claim, no exchange integration.

## Evidence
- README.md declares ARCHIVE QUEUE, Claim 0, not a product.
- `.github/workflows/pytest.yml` present; latest runs conclusion success.
- Tests in `tests/` cover decision rules, webhook, CSV paths.
- docs/SWEEP-280.md records prior CI success.
- In ADL-Governance `docs/archive_queue.md`.
- No live broker, no unsupported claims.

## Termination
For ARCHIVED class: docs present, CI green, no critical issues, no unsupported claims. GitHub archive flag remains operator-only.

Governing source: https://github.com/beyond-repair/ADL-Governance
