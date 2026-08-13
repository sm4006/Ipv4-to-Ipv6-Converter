# Ipv4-to-Ipv6-Converter

[![CI](https://github.com/sm4006/Ipv4-to-Ipv6-Converter/actions/workflows/ci.yml/badge.svg)](https://github.com/sm4006/Ipv4-to-Ipv6-Converter/actions/workflows/ci.yml)
[![CodeQL](https://github.com/sm4006/Ipv4-to-Ipv6-Converter/actions/workflows/codeql.yml/badge.svg)](https://github.com/sm4006/Ipv4-to-Ipv6-Converter/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A simple, dependency-free, **open-source** Python script that reads an
IPv4 address from the user, validates it, classifies it, converts it to
binary and back, and converts it into an IPv4-mapped IPv6 address shown in
three formats.

This project is open source under the [MIT License](LICENSE) — contributions,
forks, and issues are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) to get
started and [SECURITY.md](SECURITY.md) for the vulnerability reporting policy.

## What the script does

1. **Reads** an IPv4 address typed in by the user (`A.B.C.D`).
2. **Validates** it — checks that there are exactly 4 dot-separated numbers
   and that each one is between 0 and 255.
3. **Classifies** the address as Class A, B, C, D, or E, based on standard
   IPv4 addressing theory.
4. **Converts** the valid dotted-decimal address to dotted-binary, then
   converts that binary form back to dotted-decimal, so you can see the
   round trip.
5. **Converts** the IPv4 address into its IPv6-mapped equivalent and prints
   it in three different formats (expanded, compressed, and mixed).

## Requirements

- Python 3.7 or later
- No third-party packages — only the Python standard library is used.

## How to run it

1. Clone or download this repository:

   ```bash
   git clone https://github.com/<your-username>/ip-converter.git
   cd ip-converter
   ```

2. Run the script:

   ```bash
   python3 ip_converter.py
   ```

3. When prompted, type an IPv4 address and press Enter:

   ```text
   Enter an IPv4 address (A.B.C.D): 192.0.2.1
   ```

4. The script prints the validity check, class, binary round-trip, and the
   three IPv6 formats.

### Example run

```text
$ python3 ip_converter.py
Enter an IPv4 address (A.B.C.D): 192.0.2.1

'192.0.2.1' is a valid IPv4 address.
Class            : Class C
Dotted Binary    : 11000000.00000000.00000010.00000001
Back to Decimal  : 192.0.2.1
Round-trip check : OK

IPv4-mapped IPv6 address:
  1. Expanded form   : 0000:0000:0000:0000:0000:ffff:c000:0201
  2. Compressed form : ::ffff:c000:201
  3. Mixed form      : ::ffff:192.0.2.1
```

### Example run with an invalid address

```text
$ python3 ip_converter.py
Enter an IPv4 address (A.B.C.D): 999.1.1.1

'999.1.1.1' is NOT a valid IPv4 address.
An address must have 4 dotted numbers, each between 0 and 255.
```

## Documentation

For the basics of IPv4 and IPv6, why both exist, worked examples, and a
short bonus Q&A, see the project **[Wiki](../../wiki)**.

## Running the tests

The core logic (validation, classification, binary round-trip, and IPv6
conversion) is covered by an automated test suite so changes can be
verified without manually typing addresses each time.

```bash
pip install -r requirements-dev.txt
pytest -v
```

The same tests, plus a `flake8` lint check and a CodeQL security scan, run
automatically on every push and pull request via GitHub Actions (see the
badges above and the workflows in [`.github/workflows/`](.github/workflows)).

## Security

- The script has **zero runtime dependencies** — only the Python standard
  library — which minimizes supply-chain risk.
- **Dependabot** keeps GitHub Actions and any dev dependencies patched
  ([`.github/dependabot.yml`](.github/dependabot.yml)).
- **CodeQL** static analysis scans the code on every push, pull request,
  and weekly on a schedule.
- All address parsing validates input strictly and rejects malformed data
  rather than attempting to "recover" from it.

See [SECURITY.md](SECURITY.md) for the full policy and how to report a
vulnerability privately.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md)
for setup instructions and guidelines, and note that this project follows
the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is open source, licensed under the **MIT License** — see
[LICENSE](LICENSE) for the full text. You're free to use, modify, and
redistribute it, including for commercial purposes, as long as the license
and copyright notice are included.
