"""Minimal Kalshi trade-api/v2 client with RSA-PSS request signing.

Credentials are never stored in this repo. They are read from:
  - KALSHI_API_KEY_ID env var, or file at KALSHI_API_KEY_ID_PATH
    (default /root/.kalshi/api_key_id)
  - KALSHI_PRIVATE_KEY_PATH (default /root/.kalshi/key.pem)
"""

import base64
import json
import os
import time
import uuid

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

BASE = "https://api.elections.kalshi.com"
API = "/trade-api/v2"


class Kalshi:
    def __init__(self):
        key_id = os.environ.get("KALSHI_API_KEY_ID")
        if not key_id:
            with open(os.environ.get("KALSHI_API_KEY_ID_PATH", "/root/.kalshi/api_key_id")) as f:
                key_id = f.read().strip()
        self.key_id = key_id
        pem_path = os.environ.get("KALSHI_PRIVATE_KEY_PATH", "/root/.kalshi/key.pem")
        with open(pem_path, "rb") as f:
            self.priv = serialization.load_pem_private_key(f.read(), password=None)
        self.s = requests.Session()

    def _headers(self, method, path):
        ts = str(int(time.time() * 1000))
        msg = (ts + method + path.split("?")[0]).encode()
        sig = self.priv.sign(
            msg,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH),
            hashes.SHA256(),
        )
        return {
            "KALSHI-ACCESS-KEY": self.key_id,
            "KALSHI-ACCESS-SIGNATURE": base64.b64encode(sig).decode(),
            "KALSHI-ACCESS-TIMESTAMP": ts,
            "Content-Type": "application/json",
        }

    def _req(self, method, path, body=None, retries=3):
        for attempt in range(retries):
            try:
                r = self.s.request(
                    method,
                    BASE + path,
                    headers=self._headers(method, path),
                    json=body,
                    timeout=20,
                )
                if r.status_code == 429:
                    time.sleep(0.6 * (attempt + 1))
                    continue
                if not r.ok:
                    raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:400]}")
                return r.json() if r.text else {}
            except requests.RequestException:
                if attempt == retries - 1:
                    raise
                time.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"{method} {path}: retries exhausted")

    def get(self, path):
        return self._req("GET", API + path)

    # --- portfolio ---
    def balance(self):
        return self.get("/portfolio/balance")

    def positions(self):
        return self.get("/portfolio/positions?settlement_status=unsettled&limit=200")

    def orders(self, status="resting"):
        return self.get(f"/portfolio/orders?status={status}&limit=200")

    def fills(self, ticker=None, limit=100):
        q = f"/portfolio/fills?limit={limit}"
        if ticker:
            q += f"&ticker={ticker}"
        return self.get(q)

    # --- market data (public) ---
    def market(self, ticker):
        return self.get(f"/markets/{ticker}")["market"]

    def markets(self, event_ticker=None, series_ticker=None, status=None, limit=200, cursor=None):
        q = f"/markets?limit={limit}"
        if event_ticker:
            q += f"&event_ticker={event_ticker}"
        if series_ticker:
            q += f"&series_ticker={series_ticker}"
        if status:
            q += f"&status={status}"
        if cursor:
            q += f"&cursor={cursor}"
        return self.get(q)

    def all_markets(self, **kw):
        out, cursor = [], None
        while True:
            resp = self.markets(cursor=cursor, **kw)
            out += resp.get("markets", [])
            cursor = resp.get("cursor")
            if not cursor:
                return out

    def orderbook(self, ticker, depth=10):
        return self.get(f"/markets/{ticker}/orderbook?depth={depth}")["orderbook"]

    def event(self, event_ticker):
        return self.get(f"/events/{event_ticker}?with_nested_markets=true")

    def events_in_series(self, series_ticker, status="open"):
        out, cursor = [], None
        while True:
            q = f"/events?series_ticker={series_ticker}&status={status}&limit=200"
            if cursor:
                q += f"&cursor={cursor}"
            resp = self.get(q)
            out += resp.get("events", [])
            cursor = resp.get("cursor")
            if not cursor:
                return out

    # --- trading ---
    def create_order(self, ticker, action, side, count, price_cents, client_order_id=None,
                     order_type="limit", expiration_ts=None):
        """action: buy|sell, side: yes|no, price_cents applies to the chosen side."""
        body = {
            "ticker": ticker,
            "action": action,
            "side": side,
            "count": count,
            "type": order_type,
            "client_order_id": client_order_id or str(uuid.uuid4()),
        }
        if order_type == "limit":
            body["yes_price" if side == "yes" else "no_price"] = price_cents
        if expiration_ts:
            body["expiration_ts"] = expiration_ts
        return self._req("POST", API + "/portfolio/orders", body)

    def cancel_order(self, order_id):
        return self._req("DELETE", API + f"/portfolio/orders/{order_id}")


def taker_fee_cents(price_cents, count):
    """General Kalshi taker fee: ceil(0.07 * p * (1-p)) per contract, in cents."""
    import math
    p = price_cents / 100.0
    return math.ceil(7 * price_cents * (100 - price_cents) * count / 10000)


if __name__ == "__main__":
    k = Kalshi()
    print(json.dumps(k.balance(), indent=2))
