# Security & Privacy

ARX UI Spec analyzes visual product material that may contain confidential information.

## Sensitive inputs

Treat screenshots and design exports as potentially containing:

- personal information
- customer/company data
- internal project names
- private URLs
- access tokens or credentials
- unreleased product designs
- proprietary brand assets

Do not publish, commit, or reproduce sensitive source material into a public repository unless the owner explicitly authorizes it and it is necessary.

## Output minimization

Extract only information relevant to the UI specification task. A design spec generally does not need to repeat document contents, user records, account identifiers, secrets, or unrelated business data visible in a screenshot.

## Secret handling

If credentials or secrets are visible, do not copy them into generated specs. Describe the affected UI generically and recommend rotating exposed credentials when appropriate.

## Reporting a vulnerability

For security issues in this repository or its packaging, open a private security report through GitHub's security reporting features when available rather than publishing exploit details in a public issue.
