# Hacker News factual outline: write the final submission manually

Do not paste generated launch copy into Hacker News. Re-check current HN guidelines immediately before submitting.

Facts to use in your own words:
- Name: Evidock
- Open source, MIT
- Agent Skill for repository launch readiness
- Input: local repository or GitHub URL
- Front Door audit separates what visitors can see from what an agent can infer from source
- Claim Verification: VERIFIED / INFERRED / UNKNOWN / CONTRADICTED
- Proof Mode records exact execution scope and limitations
- Deterministic Launch Score; only PASS earns points; N_A earns zero
- Fix Mode: baseline → minimal evidence-backed patch → verify → re-audit → diff
- Outputs: audit.json, card.svg, report.html, diff.svg, badge.svg/badge.md
- Agent-facing helpers use Python standard library only
- URL inspection is static/read-only and never claimed as runtime proof
- Repository: https://github.com/davijardimn/evidock
