# Kalshi World Cup 2026 Trading

Autonomous trading toolkit for the 2026 World Cup on Kalshi.

- `STRATEGY.md` — where the edge is, position policy, fee model
- `TRADELOG.md` — every order with rationale
- `kalshi_client.py` — signed REST client (RSA-PSS, trade-api/v2)
- `scripts/survey.py` — market landscape snapshot (games, boards, books)
- `scripts/monitor.py` — poll fills/prices, append snapshots to `data/`

## Credentials

Never stored in this repo. The client reads:

- `KALSHI_API_KEY_ID` (or file at `KALSHI_API_KEY_ID_PATH`, default
  `/root/.kalshi/api_key_id`)
- `KALSHI_PRIVATE_KEY_PATH` (default `/root/.kalshi/key.pem`)

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install cryptography requests
.venv/bin/python kalshi_client.py   # prints balance if auth works
.venv/bin/python scripts/survey.py
```
