#!/usr/bin/env python3
"""Maintenance lint: body budget, reference map, and facts written in two places.

usage: lint.py [SKILL_DIR] [--stats]
exit 0 clean, 1 findings, 2 bad input. One finding per line.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

BODY_MAX = 13000  # bytes; the body loads on every activation
MIN_WORDS = 5  # a shorter literal is vocabulary, a longer one is a finding


def literals(text):
    return {" ".join(m.split()) for m in re.findall(r"`([^`\n]+)`", text) if len(m.split()) >= MIN_WORDS}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--help" in sys.argv or len(args) > 1:
        print(__doc__.strip())
        return 0 if "--help" in sys.argv else 2
    root = Path(args[0]) if args else Path(__file__).resolve().parent.parent
    body = root / "SKILL.md"
    if not body.is_file():
        print(f"error: no SKILL.md in {root}")
        return 2
    refs = sorted((root / "references").glob("*.md"))
    text = {p: p.read_text() for p in [body, *refs]}
    out = []

    size = len(text[body].encode())
    if size > BODY_MAX:
        out.append(f"SKILL.md is {size} bytes, budget {BODY_MAX}: move a recipe to its reference")

    for p in refs:
        if f"references/{p.name}" not in text[body]:
            out.append(f"references/{p.name} is never named in SKILL.md, so nothing loads it")
    for p, t in text.items():
        for name in set(re.findall(r"references/([\w.-]+\.md)", t)):
            if not (root / "references" / name).is_file():
                out.append(f"{p.name} points at references/{name}, which does not exist")
        for name, head in re.findall(r'`references/([\w.-]+\.md)`, "([^"]+)"', t):
            target = (root / "references" / name).read_text() if (root / "references" / name).is_file() else ""
            if not re.search(rf"^#+ {re.escape(head)}", target, flags=re.M):
                out.append(f'{p.name} points at "{head}" in references/{name}: no such heading')

    # example prompts in fenced blocks reuse vocabulary on purpose
    flat = {p: " ".join(re.sub(r"```.*?```", "", t, flags=re.S).split()) for p, t in text.items()}
    homes = defaultdict(set)
    for p, t in text.items():
        for lit in literals(t):
            homes[lit].update(q.name for q in flat if lit in flat[q])
    dups = {lit: names for lit, names in homes.items() if len(names) > 1}
    for lit, names in sorted(dups.items()):
        out.append(f"two homes ({', '.join(sorted(names))}): `{lit}`")

    if "--stats" in sys.argv:
        total = sum(len(t.encode()) for t in text.values())
        print(f"body {size} B, references {total - size} B in {len(refs)} files, {len(dups)} literals with two homes")
    print("\n".join(out))
    return 1 if out else 0


if __name__ == "__main__":
    sys.exit(main())
