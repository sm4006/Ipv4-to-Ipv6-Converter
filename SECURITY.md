# Security Policy

## Supported Versions

This is a small, single-file educational utility. The `main` branch is the
only supported version — please always use the latest commit.

| Version | Supported |
| ------- | --------- |
| `main`  | ✅ |
| older tags / forks | ❌ |

## Reporting a Vulnerability

This project only performs local string parsing and arithmetic on
user-supplied text (no network calls, no file I/O, no external
dependencies), so its attack surface is intentionally small. That said, if
you find a security issue — for example, an input that causes a crash,
excessive resource use, or unexpected behavior that could be abused — please
report it responsibly:

1. **Do not open a public issue for security reports.**
2. Use GitHub's **[private vulnerability reporting](../../security/advisories/new)**
   feature (Security tab → "Report a vulnerability") so the maintainers can
   triage before any details are made public.
3. Include:
   - A description of the issue and its potential impact
   - Steps to reproduce (a sample input is usually enough for this project)
   - Your suggested fix, if you have one

You should receive an initial response within a few days. Once a fix is
available, it will be released and the advisory will be published with
credit to the reporter (unless you prefer to remain anonymous).

## Scope

In scope:
- `ip_converter.py` and any future source files in this repository
- The GitHub Actions workflows in `.github/workflows/`

Out of scope:
- Issues in your local Python interpreter, OS, or terminal
- Third-party tools you use to run or package this script

## Security Practices in This Repository

- **No runtime dependencies.** The script only uses the Python standard
  library, minimizing supply-chain risk.
- **Dependabot** is enabled (see [`dependabot.yml`](.github/dependabot.yml))
  to keep GitHub Actions versions and any future dependencies patched.
- **CodeQL static analysis** runs automatically on every push and pull
  request (see [`codeql.yml`](.github/workflows/codeql.yml)) to catch
  common security issues in Python code.
- **Input validation** — all address parsing rejects malformed input
  (wrong number of fields, out-of-range values, non-numeric characters)
  before any conversion logic runs, rather than trying to "recover" from
  bad input.
