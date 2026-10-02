"""Legacy path: src.local_app → fortitrade."""

from fortitrade.app import app, create_app
from fortitrade.decision import get_trade_decision

__all__ = ["app", "create_app", "get_trade_decision"]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
