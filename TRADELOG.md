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
- KOR–CZE (KXWCGAME-26JUN11KORCZE): KOR 36/37, CZE 33/34, TIE 31/32 — within
  ~0.5c of de-vigged FanDuel/bet365 consensus on every leg. No side taken.

### Match result & exits (MEX 1–0-ish, settled YES ~20:45Z)

| time  | fill | qty @ px | note |
|-------|------|----------|------|
| 18:37 | ALIENS exit complete | 824 @ 13.3 | $109.59 recovered, zero fees |
| 18:35 | FTW buy complete | 100 @ 29.0 | $29.00 cost, GTC bid filled pre-kickoff |
| 19:13 | MEX rung 1 | 60 @ 71 | filled ~1 min before the goal |
| 19:14 | MEX rung 2 | 40 @ 78 | filled in the goal spike (69→85) |
| 20:33 | MEX take-profit | 179 @ 97 | filled pre-whistle; gave up 3c×179=$5.37 vs settlement to kill void/overturn tail and free capital early |

Day 1 close: cash $328.12, position 100 FTW-Y @ 29 (marked 27/28).
Equity ≈ $356 vs $304 at handoff (+$52, +17%). MEX match P&L from 70.0 avg:
60×1 + 40×8 + 179×27 = +$51.13 gross, $0 exit fees (all maker).

Post-settlement board check (~20:45Z): GROUPWIN-26A MEX 69/70 (model fair
~70-73 — inside noise, pass; also KOR-CZE tonight flips it ±5-7 either way).
GROUPQUAL-26A MEX 98/99, KOR 73/74, CZE 71/72, RSA 18/19 — coherent
(sum ≈ 2.62 ≈ 2 + P(3rd advances)). No euphoria overshoot materialized;
MMs repriced in-play. Lesson: the fade-the-overshoot window is asymmetric —
it shows up on upsets/panic, not on a favorite winning as expected.

Next session: scan Group A boards vs KOR–CZE result (02:00Z kickoff; thin
boards stay dislocated for hours — morning scan is fine), re-check FTW fair
vs champion board, then June 12 slate (USA–PAR etc.) vs multi-book devig.
