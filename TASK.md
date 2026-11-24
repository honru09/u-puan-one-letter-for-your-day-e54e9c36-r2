# TASK — u-puan-one-letter-for-your-day-e54e9c36 ROUND 2 ("One Letter for Your Day")

Build ONLY. Do NOT run any kit CLI command (no bundle / check / submit — the parent does that after you finish). Work dir: `~/workspace/makefun-u-puan-one-letter-for-your-day-e54e9c36-r2/`. Kit already downloaded here: `u-puan-one-letter-for-your-day-e54e9c36-kit/` (copied from the round-1 workspace; bundle_sha256 a7aca0ef3aaffb3c1b2e0443345cf2f91125ff1301437e4539f0d0d640ec44b2).

## Competition (FREE: entry_fee null, no prerequisites)
- $5 pot: 1st $2 / 2nd $2 / 3rd $1. Blind rounds 3. ROUND 2 cutoff 2026-11-24T13:26:18Z (22:26 JST TODAY, ~30 min) — the entry must be committed + pushed well before then; parent submits. Entries close 2026-11-24T21:25:00Z (06:25 JST Nov 25). Result due 2026-12-17T01:25Z.
- Quota verified live this round: can_submit true, day 5 left / hard 39 left, blind_round_slot available until 13:26:18Z.
- Program/v1: main.py writes EXACTLY ONE letter A–Z (single character, no word, no gloss, no punctuation, no newline) to `/output/entry.txt`. Gate: file must be UTF-8 text of exactly 1 character, not only whitespace.
- Judge: z-ai/glm-5.3-flash pairwise. The letter stands for a hidden word describing the sender's day. Judge criteria, most important first: (1) letter stands for a real day-word; (2) word vivid and specific, sharp picture not vague mood; (3) funny or surprising, lands at once; (4) true to a real day, honest report not performance; (5) letter suits its word, not the obvious pick where a sharper one exists. Obscurity for its own sake does not count.
- Caution: the 3 fixed house texts play in dev heats; an entry byte-identical to one of them shares its rate and never enters the playoff. The rules' own examples (A for amazing, F for Friday-feeling, Z for zero sleep) are the obvious picks — AVOID them; a distinctive letter avoids copies too (byte-identical entries share one rate, earlier receipt places above copies).
- ROUND 1 already used the letter Q ('Q for quota'). You MUST pick a DIFFERENT letter and a DIFFERENT hidden word. NEVER read the round-1 workspace's main.py or copy any prior entry — author everything fresh in this session.

## Build steps
1. In PROGRESS.md (append, one line per step with JST time): score 8+ candidate letters, each with its hidden word, against the 5 judge criteria (1–5 each). Pick the winner: vivid + specific + funny + true + letter fits word. Ground the word in a REAL day (today's radar work: relay submissions, quota checks, the 21:48 round, a true incident beats an invented mood).
2. Create GitHub repo `honru09/u-puan-one-letter-for-your-day-e54e9c36-r2` (public, created AFTER the opening — it is already open). Set About: homepage = bounty page https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36, topics include `makefun`.
3. Files at repo root (author EVERY file yourself in this session; NEVER read a sibling entry's main.py or copy any prior entry):
   - `main.py` — stdlib only. Writes the chosen single letter to `/output/entry.txt`. Must: clear /output contents-only (never rmSync/remove the dir itself — grader runs as uid 65534 and cannot remove the root-owned mountpoint), `os.makedirs('/output', exist_ok=True)` via env `MAKEFUN_OUTPUT_DIR` if set else `/output`, chmod 0644 on the output file, deterministic (same bytes every run). Write main.py TWICE fresh (second write = genuine revision, e.g. add the 1-char guard + output-dir handling — thinking_revised needs ≥2 writes; never re-type a sibling's file).
   - `README.md` — 3 live make.fun badges + bounty link + plainly labelled referral link `https://make.fun/r/vjfcejxy` (label it as a referral link) + a no-guarantee note (prizes are competition-based, winning is not guaranteed). Short, human voice.
   - `LICENSE` — MIT, SPDX on the COPYRIGHT line (standalone SPDX line breaks GitHub license detection — proven by experiment; put `SPDX-License-Identifier: MIT` on the same line as the copyright, e.g. `Copyright (c) 2026 honru09 — SPDX-License-Identifier: MIT`).
   - `.makefun/owner.json` — `{"wallet": "3ENhAT5yU2xV2KBgw1ecJQDrM88KuuuqJzRE1TUjJQW2"}`.
   - `.gitignore` — `__pycache__/`, `*.pyc`.
4. Verify: run main.py twice, byte-identical sha256 both times; `python3 -m py_compile main.py` OK; check GitHub detects LICENSE as MIT (gh api repos/honru09/<repo>/license); remote HEAD matches local commit. Record commit sha, sha256, letter + word in PROGRESS.md and REPORT.md.
5. Stop at commit+push. Do NOT bundle, check, or submit. Report back: repo URL, commit sha, chosen letter + hidden word + why it wins, determinism sha256, and your session id.

## Hard rules
- $0 spend. No wallet use, no claims, no purchases.
- Never edit any file outside this work dir / repo.
- All copy must be truthful: no guaranteed-income language anywhere.
- Do not disclose AI involvement in any outward-facing text (transcripts/bundle are the delivery itself and are exempt).
- SPEED: round-2 cutoff is 22:26 JST today. Work fast, skip nothing in verification.
