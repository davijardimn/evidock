# Evidence Redaction v0.6

Evidock outputs are designed to be shareable. **Prove the finding; do not republish the secret.**

When evidence includes credentials, tokens, personal contact details, private keys, session data, or other sensitive values: record file/location and type; redact or summarize the value; do not copy plaintext passwords, API keys, cookies, auth tokens, private keys, or full secrets into shareable output; avoid repeating unnecessary personal data.

A suspicious credential may justify a blocker, but do not claim it is live unless verified safely and legitimately. Recommend rotation if reuse/exposure is plausible. Never use real credentials or production secrets just to strengthen a score.
