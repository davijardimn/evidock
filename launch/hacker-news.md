# Hacker News / Show HN notes — write this one yourself

Do **not** paste generated launch copy into Hacker News. HN's current guidelines explicitly ask users not to post generated text and not to automate posting. If you decide to submit RepoReel there, write the title and text yourself in your normal voice.

## Facts worth explaining in your own words

- You built RepoReel because repository presentation and repository reality often diverge.
- It is open source / MIT and the primary artifact is a standard Agent Skill.
- The unusual parts are Front Door separation, evidence states, scoped Proof Mode, deterministic score calculation, and validated shareable artifacts.
- The code is deliberately dependency-free Python for the agent-facing scripts.
- The CI matrix covers Linux, Windows and macOS on Python 3.9 and latest.
- A real development lesson: the first versions accidentally awarded points for vacuous conditions such as “no broken docs links” when no docs existed. That led to the explicit `N_A != PASS` rule.
- Another development lesson: one runtime check must never become a cross-platform compatibility claim, which led to the execution-scope model.

## Show HN fit check

Before submitting:

- Read the current HN and Show HN rules yourself.
- If your HN account is new or you are not familiar with the community, wait; Show HN has been restricting submissions from users who are not yet familiar with the site.
- Submit the original GitHub repository, not a marketing landing page.
- Do not ask anyone to upvote or coordinate comments.
- Stay available to answer technical questions and criticism.

The strongest HN discussion is probably not “AI roasts your README”; it is the engineering question behind RepoReel: **how much of an agent evaluation should be model judgment versus deterministic evidence and tooling?**
