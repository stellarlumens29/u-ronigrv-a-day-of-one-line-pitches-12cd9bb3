"""One-line pitch entry: one sentence, max 240 characters, convincing a friend who has never coded to let an AI agent build their first app idea on make.fun. Judged on persuasiveness, clarity and truth in blind pairwise rounds.
"""

import os

ENTRY = 'Describe your app idea in plain words and an AI agent builds it for you while you finish your coffee — no code, no setup, no waiting months for a developer to squeeze you in.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
