# krea2-prompting

Agent Skills repo: Markdown that an image-prompting agent reads, plus one Python 3 lint. `SKILL.md` loads whole on every activation; a `references/*.md` file loads only when a task opens it.

## Commands

- Full check: `python3 evals/lint.py` # body budget, reference map, section pointers, phrases quoted in two files

## Conventions

- A new finding gets one home: the section of the `references/` file it belongs to, written as the rule plus the wording that worked.
- `SKILL.md` takes that finding as one row of "When the brief contains", or as one line of "Every prompt" when it applies to nearly every image. The row says what to do in plain words; the quoted wording and the receipt stay in the reference.
- A finding that refines an existing rule edits that rule in place. It gets no section of its own.
- Point at a section in this form: `references/poses.md`, "Hands and held objects". The lint resolves that form and no other.
- Mark a finding tested only when a render showed it. An untested claim says so.
- A new reference file also gets a row in the `README.md` "What's inside" table.

## Boundaries

- Always: `python3 evals/lint.py` exits 0 before handoff.

## Pointers

- `evals/evals.json` - what a correct answer contains, per brief. Read when a finding changes the expected answer.
