# World Cup 2026 — Kalshi Trading Strategy

Mandate: maximize returns during the tournament (Jun 11 – Jul 19, 2026), full
discretion. Starting book (Jun 11, ~17:00Z): $0.69 cash, 279 YES
`KXWCGAME-26JUN11MEXRSA-MEX` @ 70c avg (Mexico to beat South Africa in the
opener), 824 YES `KXALIENS-27` @ 17.1c avg. Total equity ≈ $304.

## Where the edge is (and isn't)

Checked Jun 11: Kalshi's WC **match markets and champion board are efficient** —
match mids sit exactly on de-vigged sportsbook consensus (verified vs
FanDuel/DraftKings/bet365 for MEX-RSA, USA-PAR, CAN-BIH) and the champion board
tracks books with 0.1–0.3c spreads and 5–11M volume per team. Do not pay
spread+fees to take sides there without independent information.

Edges actually identified, in priority order:

1. **Mispriced non-sports inventory.** `KXALIENS-27` ("U.S. confirms aliens
   exist before 2027") trades 13.2/13.3 vs a true probability near zero — a
   meme premium worth harvesting. Selling the 824-lot recovers ~$110 of dead
   capital (expected settlement value ≈ $0) to fund tournament trading.
2. **Derivative/novelty boards vs the champion board.** Retail trades the
   novelty boards without doing the arithmetic against the main board.
   Found live: First-Time Winner 28/30 vs ~32–33 fair (sum of never-won
   contenders: POR 10.85, NED 5.05, MEX 2.45, NOR 2.45, BEL 2.25, COL 1.85,
   JPN 1.65, USA 1.55, MAR 1.55, SUI/TUR ~1.9 + tails). Continent board and
   NOEURSA checked — consistent, no trade.
3. **Maker-only execution.** Taker fee is 7% of p(1−p) (≈1.5–1.75c near
   50c); maker is free on these series. Never cross a spread without an
   explicit reason; rest orders at or inside the touch and let flow come.
4. **Event-driven dislocations.** Post-goal/post-match overshoots in
   correlated boards (group winner, qualifiers, ladders) lag the match
   markets by minutes. Keep cash to fade panic/euphoria after results.

## Position policy

- The Mexico opener bet is the user's thesis trade at a fair price — keep
  the core, monetize hype: sell-the-rip ladder 60@71, 40@78 (maker), hold
  ~179 to settlement with a 97c take-profit (preserves the user's original
  exit intent, resized so total sells ≤ position).
- No naked shorts of longshots (capital-inefficient on Kalshi: collateral =
  100−price). Shorts only via cheap NO with a concrete arithmetic edge ≥4c.
- Keep ≥$20 cash buffer for post-match dislocations.
- Every order gets logged in TRADELOG.md with rationale at placement time.

## Fee model

taker_fee = ceil(0.07 × price × (100−price) × n) per fill, maker = 0.
A round-trip taker at 50c costs ~3.5c/contract — half the typical edge.
This is why everything above says "maker".
