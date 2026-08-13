# Contributing to ip-converter

Thanks for your interest in improving this project! It's a small,
dependency-free educational tool, so contributions of all sizes are welcome
— typo fixes, new test cases, and feature additions alike.

## Getting started

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/Ipv4-to-Ipv6-Converter.git
   cd Ipv4-to-Ipv6-Converter
   ```

2. **Create a branch** for your change:

   ```bash
   git checkout -b my-fix-or-feature
   ```

3. **Install dev dependencies** (only needed for linting/testing, the
   script itself has no runtime dependencies):

   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Make your changes.** Keep functions small and testable — the script is
   organized so each step (validate, classify, convert) is its own function.

5. **Run the test suite and linter** before opening a PR:

   ```bash
   pytest -v
   flake8 ip_converter.py tests/ --max-line-length=100
   ```

6. **Add tests** for any new behavior in `tests/test_ip_converter.py`.

7. **Commit and push**, then open a pull request against `main`. Please
   describe what you changed and why.

## Reporting bugs / requesting features

Please use the issue templates under **Issues → New Issue**. Include:

- What you expected to happen
- What actually happened
- The exact input that triggered the issue (for bugs)

## Reporting security issues

Please **do not** open a public issue for security vulnerabilities — see
[SECURITY.md](SECURITY.md) for how to report them privately.

## Code style

- Follow standard PEP 8 formatting (enforced by `flake8` in CI).
- Prefer clear, descriptive names over cleverness — this project is used
  for learning IPv4/IPv6 concepts, so readability matters as much as
  correctness.
- Keep the standard-library-only, zero-dependency design unless there's a
  strong reason to add a dependency (and if so, please discuss it in an
  issue first).

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By
participating, you agree to uphold it.

## License

By contributing, you agree that your contributions will be licensed under
the project's [MIT License](LICENSE).
