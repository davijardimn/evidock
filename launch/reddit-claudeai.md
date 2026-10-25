# I built Evidock — an evidence-first repository launch reviewer for Claude

I built Evidock because a project can be technically solid and still be almost impossible for a stranger to understand, trust, or try from its GitHub page.

Evidock is a free/open-source Agent Skill. Give Claude a local repository or GitHub URL and it audits the repository's Front Door, verifies consequential README claims, runs small scoped Proof Mode checks when execution is available, computes a deterministic Launch Score, and can fix evidence-backed launch blockers before re-auditing.

The important constraint is that it cannot invent proof to improve the score. Remote URL inspection is labeled static evidence; `N_A` earns zero; contradicted claims stay contradicted until the evidence changes.

It can also generate a card, HTML report, before/after diff, and static badge from validated `audit.json`.

Repo: https://github.com/davijardimn/evidock

The line I use to keep the project honest: **Market the evidence. Never manufacture it.**
