# Trade Log

All times UTC. Prices in cents. Fees: maker 0, taker 7%·p(1−p).

## 2026-06-11 (opening day)

Inherited book: 279 YES KXWCGAME-26JUN11MEXRSA-MEX @ 70.0 avg (user buy,
taker, $4.10 fees, 16:39Z); 824 YES KXALIENS-27 @ 17.1 avg; $0.69 cash.
Two stale user GTC asks found: 279 MEX @ 97, 824 ALIENS @ 98.

| time  | action | market | qty @ px | why |
|-------|--------|--------|----------|-----|
| 17:12 | SELL YES (maker ask, GTC) | KXALIENS-27 | 824 @ 13.3 | True prob ≈ 0, market pays 13.3 for meme risk; frees ~$110 dead capital for tournament. EV ≈ +$100 vs holding to settlement. |
| 17:13 | SELL YES (maker ask) | KXWCGAME-26JUN11MEXRSA-MEX | 60 @ 71 | Trim ladder above 70 entry: zero-fee, fills only into pre-match/in-play Mexico flow. Cuts single-match variance (was 64% of equity) at positive price vs entry. |
| 17:13 | SELL YES (maker ask) | KXWCGAME-26JUN11MEXRSA-MEX | 40 @ 78 | Second rung: monetizes an in-play overshoot on a Mexico goal. |
| 17:33 | CANCEL | user's 279 MEX @ 97 + 824 ALIENS @ 98 | — | Combined with new orders they would oversell into naked shorts (379 vs 279 owned; 1648 vs 824). |
| 17:33 | SELL YES (maker ask) | KXWCGAME-26JUN11MEXRSA-MEX | 179 @ 97 | Re-place user's take-profit intent, resized to what the ladder leaves uncovered. |
| 17:36 | BUY YES (maker bid, GTC) | KXWC1STTIMEWIN-26-Y | 100 @ 29 | First-Time Winner 28/29 vs ~32–33 fair from champion-board arithmetic (POR+NED+MEX+NOR+BEL+COL+JPN+USA+MAR+… never-won sum). +3–4c maker edge, resolves end of tournament. |

Status 17:36Z: aliens 327/824 filled @ 13.3; cash $40.74 (incl. $29 reserved
for FTW bid). MEX book 69/70 unchanged; kickoff 19:00Z.

Passed on (documented so future sessions don't re-litigate):
- USA 49/50 and CAN 53/54 openers: exactly at de-vigged book consensus.
- Mexico Group A winner 58/59 vs ~54 bet365-fair: single-source, and Mexico
  plays all 3 group games at Azteca altitude — book may be stale, not Kalshi.
- Continent board / NOEURSA / host-KO markets: arithmetically consistent
  with champion board after fees; sell-side "arb" loses to taker fees and
  collateral drag.
