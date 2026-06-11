"""Snapshot the World Cup market landscape: portfolio, today's games, boards."""

import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, __file__.rsplit("/", 2)[0])
from kalshi_client import Kalshi


def cents(m, field):
    v = m.get(field + "_dollars")
    return float(v) * 100 if v not in (None, "") else 0.0


def quote(m):
    return f"{cents(m, 'yes_bid'):5.1f}/{cents(m, 'yes_ask'):5.1f}"


def main():
    k = Kalshi()

    print("=== PORTFOLIO ===")
    print(" cash:", k.balance().get("balance_dollars"))
    for p in k.positions().get("market_positions", []):
        print(f" {p['ticker']:36s} pos={p['position_fp']:>10s} cost=${p['total_traded_dollars']}")
    for o in k.orders().get("orders", []):
        print(f" order {o['ticker']:30s} {o['action']:4s} {o['side']:3s} "
              f"{float(o.get('remaining_count_fp', 0)):8.2f} left @ y{o.get('yes_price_dollars')}")

    print("\n=== GAMES (next 2 days) ===")
    today = datetime.now(timezone.utc)
    tags = {(today + timedelta(days=d)).strftime("26%b%d").upper() for d in (0, 1)}
    for e in k.events_in_series("KXWCGAME", status="open"):
        et = e["event_ticker"]
        if any(t in et for t in tags):
            ms = k.event(et)["event"].get("markets", [])
            legs = "  ".join(f"{m.get('subtitle') or 'Tie'}={quote(m)}" for m in ms)
            print(f" {et:34s} {legs}")

    print("\n=== CHAMPION BOARD (ask >= 1c) ===")
    ms = k.event("KXMENWORLDCUP-26")["event"].get("markets", [])
    ms.sort(key=lambda m: -(cents(m, "yes_bid") + cents(m, "yes_ask")))
    for m in ms:
        if cents(m, "yes_ask") >= 1:
            print(f" {m.get('subtitle') or m.get('yes_sub_title', ''):22s} {quote(m)}")

    print("\n=== NOVELTY BOARDS ===")
    for et in ["KXWC1STTIMEWIN-26", "KXWCNOEURSA-26", "KXWCCONTINENT-26", "KXWCHOSTKO-26"]:
        ms = k.event(et)["event"].get("markets", [])
        legs = "  ".join(f"{m.get('subtitle') or m.get('yes_sub_title', '')}={quote(m)}" for m in ms)
        print(f" {et:22s} {legs}")


if __name__ == "__main__":
    main()
