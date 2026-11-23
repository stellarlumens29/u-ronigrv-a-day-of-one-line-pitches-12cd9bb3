# A Day of One-Line Pitches

make.fun bounty: https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

One fixed entry written by `main.py` (Python 3, standard library only) to `/output/entry.txt`:

> Describe your app idea in plain words and an AI agent builds it for you while you finish your coffee — no code, no setup, no waiting months for a developer to squeeze you in.

The pitch leads with the friend's own words (plain words, no code), names the concrete payoff (a built app by the time coffee is done) and removes the three classic objections in one breath: no code, no setup, no waiting months for a developer. It stays truthful: it promises a first version built from a description, not a finished company.

Length: 174 characters (gate: 1–240).

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

Deterministic: two runs write byte-identical output. No network.
