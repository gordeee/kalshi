"""Poll portfolio + watched markets, append JSONL snapshots to data/.

Usage: monitor.py [minutes] [interval_sec]   (defaults: 240, 180)
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, __file__.rsplit("/", 2)[0])
from kalshi_client import Kalshi

WATCH = [
    "KXWCGAME-26JUN11MEXRSA-MEX",
    "KXWCGAME-26JUN11MEXRSA-TIE",
    "KXWCGAME-26JUN11MEXRSA-RSA",
    "KXALIENS-27",
    "KXWC1STTIMEWIN-26-Y",
]


def snap(k):
    row = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    row["cash"] = k.balance().get("balance_dollars")
    row["positions"] = {
        p["ticker"]: p["position_fp"] for p in k.positions().get("market_positions", [])
    }
    row["orders"] = [
        {
            "ticker": o["ticker"],
            "px": o.get("yes_price_dollars"),
            "left": o.get("remaining_count_fp"),
        }
        for o in k.orders().get("orders", [])
    ]
    row["quotes"] = {}
    for t in WATCH:
        try:
            m = k.market(t)
            row["quotes"][t] = f"{m.get('yes_bid_dollars')}/{m.get('yes_ask_dollars')}"
        except Exception as e:
            row["quotes"][t] = f"err:{str(e)[:40]}"
    return row


def main():
    minutes = float(sys.argv[1]) if len(sys.argv) > 1 else 240
    interval = float(sys.argv[2]) if len(sys.argv) > 2 else 180
    out = os.path.join(os.path.dirname(__file__), "..", "data", "snapshots")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, datetime.now(timezone.utc).strftime("%Y%m%d") + ".jsonl")
    k = Kalshi()
    deadline = time.time() + minutes * 60
    while time.time() < deadline:
        try:
            row = snap(k)
            with open(path, "a") as f:
                f.write(json.dumps(row) + "\n")
            print(row["ts"], row["cash"], row["quotes"].get(WATCH[0]), flush=True)
        except Exception as e:
            print("snap error:", str(e)[:120], flush=True)
        time.sleep(interval)


if __name__ == "__main__":
    main()
