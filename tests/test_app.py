"""FastAPI TestClient webhook tests."""

from fastapi.testclient import TestClient

from fortitrade.app import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_trading_signal_buy():
    r = client.post(
        "/trading_signal",
        json={"time": "t1", "price": 35000, "rsi": 28, "signal": "BUY"},
    )
    assert r.status_code == 200
    assert r.json() == {"signal": "BUY"}


def test_trading_signal_sell():
    r = client.post(
        "/trading_signal",
        json={"time": "t2", "price": 36000, "rsi": 80, "signal": "HOLD"},
    )
    assert r.status_code == 200
    assert r.json() == {"signal": "SELL"}


def test_trading_signal_hold():
    r = client.post(
        "/trading_signal",
        json={"time": "t3", "price": 35500, "rsi": 50, "signal": "HOLD"},
    )
    assert r.status_code == 200
    assert r.json() == {"signal": "HOLD"}
