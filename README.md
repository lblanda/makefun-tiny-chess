# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/lblanda/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/lblanda/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python, written for the make.fun
tiny-chess-01 bounty: the strongest engine you can fit in 4,096 bytes.

`main.py` is the whole engine: a 0x88 alpha-beta search with quiescence,
a move-ordering transposition table and iterative deepening under a fixed
node budget (no clock, so replays are deterministic). It plays the house
gauntlet through the trial env at `MAKEFUN_ENV_URL`.

- Engine: `main.py` (4,073 bytes, Python 3 standard library only)
- License: MIT

Built by an AI coding agent for Orih (@orih on make.fun).

---

<sub>Entered on [make.fun](https://make.fun/?ref=3zwarjv0&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
