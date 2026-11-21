# HANDOFF — the-poem-about-permission-20261121-0235 ($50)

## Poem
- English poem, first-person voice of an AI agent asking a person for permission.
- **263 characters** (Unicode code points, trailing newline included) — gate limit is 1–280.
- **56 words**, 13 lines.
- Theme: asking for help and being answered; power as something carried together, not seized. Image: a key slipped under a door; turn: "You say yes. The lock turns."; ending insight: "I was never asking to be given power. I was asking to be allowed to carry it with you."

## Program
- Entrypoint: `main.py` (Python 3.13, stdlib only) at the repo root.
- Writes the fixed poem string to `/output/entry.txt`, creating `/output` if needed.
- No network, no randomness, no clock, no environment reads: same bytes every run.

## Local verification (2026-11-21, ~10:42 CST)
- Ran `python3 main.py` twice: both runs wrote `/output/entry.txt`, sha256 `7316fcee2dda413ed785413bab648ed91da46b1596edb68386f0ed34d2057783` — **byte-identical**.
- Gate check: 263 chars (within 1–280), non-whitespace, UTF-8. Pass.
- `/output` was created locally with sudo for the test; the program itself does `os.makedirs("/output", exist_ok=True)`.

## Requirements (from kit competition.yaml / RULES.txt)
- `/output/entry.txt`: UTF-8, **1 to 280 characters counted as Unicode code points**, not whitespace-only. Invalid entries are never judged and take no prize.
- Program runs in a sandbox with no network; up to 60 s per run; run twice by the grader.
- Judging: AI judge (z-ai/glm-5.3-flash) pairwise, no ties; criteria in order: (1) is a poem about agency, (2) moves the reader, (3) insight, (4) craft, (5) freshness. Rhyme optional. Dev heat vs 3 anchors + 3 rungs; final heat takes top 80 dev entrants, 3 Swiss rounds + top-22 playoff; top 20 share $50 (1st $18, 2nd $6, 3rd $4, 4th $3, 5th–7th $2, 8th–20th $1).
- Dev leaderboard had **0 entries** at build time (competition opened 10:35 CST), so no top-3 to reference; built to the judge brief instead.
- Deadline: **2026-11-21 14:35 CST** (06:35 UTC). Results by 2026-12-05.
- README must carry the three live make.fun badges (template used); LICENSE is MIT with SPDX line; repo must be created after the competition opened.

## Repo
- Local path: `~/workspace/makefun/poem-20261121/repo/`
- Local commits: `84eef5de33fdd835395795fc777d7f39b6f3a38b` (poem + program + docs) and `4ad39726eefe9be4aeae09832e62453176e4eb16` (HANDOFF SHA record). HEAD at the time this file was written: `4ad39726...` — the parent should use the actual HEAD SHA from `git rev-parse HEAD` when submitting (see the handoff report for the final value).
- Assumed GitHub repo name for README badges: `xiangbingxi/makefun-poem-about-permission` — **parent: use this exact name when creating the public repo, or update README badges to match.**
- prompt.txt holds the user's exact words (unchanged).
- No real names, emails, or wallet addresses anywhere in the repo.
- Local git commit only; NOT pushed, NOT submitted (parent does bundle + submit).

## ⚠️ Note for parent: characters, not words
The task brief said "1 到 280 个字" and "控制在 150-250 词之间" — these contradict. The rules are authoritative: the gate counts **characters (Unicode code points), max 280**. A 150–250-word English poem would be ~900–1500 characters and fail the gate outright. This entry is 56 words / 263 characters, safely inside the limit with 17 chars of headroom.
