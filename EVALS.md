# Security Evaluations

## Workstream A — Secure CI/CD Pipeline

### A1 — Python dependency vulnerability scan

**Scenario:** A Python dependency contains a known vulnerability.

**Expected:** `pip-audit` detects the vulnerable dependency and the CI job fails.

**Observed:** `pip-audit` runs successfully against the current project dependencies. No known vulnerabilities were reported.

**Status:** Observed

---

### A2 — Secret detection

**Scenario:** A developer accidentally commits a credential or API key.

**Expected:** Gitleaks detects the secret and the CI job fails.

**Observed:** Gitleaks is configured and runs against the repository Git history. A safe synthetic secret fixture is maintained locally for evaluation without committing credentials to the repository.

**Status:** Observed

---

### A3 — Static application security testing

**Scenario:** Application code contains an insecure pattern such as a hardcoded secret.

**Expected:** Semgrep detects the insecure pattern and the CI job fails.

**Observed:** Semgrep runs the standard Python rules and the custom hardcoded-secret rule in `policies/semgrep/python-security.yml`.

**Status:** Observed

---

### A4 — Container vulnerability scanning

**Scenario:** The Docker image contains a known HIGH or CRITICAL vulnerability.

**Expected:** Trivy detects HIGH/CRITICAL vulnerabilities and the CI job fails.

**Observed:** The application image is built in GitHub Actions and scanned with Trivy using HIGH and CRITICAL severity levels. Unfixed vulnerabilities are ignored.

**Status:** Observed