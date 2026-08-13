# IPv4 & IPv6 Basics — Why We Need Them, Examples, and Bonus Q&A

> Wiki page for the `ip-converter` repository. This page covers the
> background concepts behind `ip_converter.py`: what IPv4 and IPv6 are, why
> both exist, simple worked examples, and a short bonus Q&A section.
>
> Direct quotations from research sources are shown in quotation marks with
> the source named right next to them. Everything else is written in plain
> language for quick reading.

## Table of Contents

1. [IPv4 Basics](#1-ipv4-basics)
2. [IPv6 Basics](#2-ipv6-basics)
3. [Why We Need Both](#3-why-we-need-both)
4. [Simple Examples](#4-simple-examples)
5. [Bonus Questions & Answers](#5-bonus-questions--answers)
6. [References / Relevant Links](#references--relevant-links)

---

## 1. IPv4 Basics

**IPv4 (Internet Protocol version 4)** is the original addressing system the
Internet was built on. A recent research survey describes it this way:
**"IPv4, introduced in the 1980s, is a crucial part of the TCP/IP suite,
identifying hosts using logical addresses"** and it works at the network
layer to help route data (Hossain, Binti & Uddin, 2024).

**Key facts:**

- An IPv4 address is **32 bits** long.
- It's written as **4 numbers separated by dots**, e.g. `192.0.2.1` — this is
  called *dotted-decimal notation*.
- Each of the 4 numbers is one **byte** (8 bits), so it can only range from
  **0 to 255**.
- Total possible addresses: 2³² = **4,294,967,296** — as one survey puts it,
  **"IPv4 uses a 32-bit addressing which amounts to 4,294,967,296 unique
  addresses"** (Hossain, Binti & Uddin, 2024).

**Address classes** — early IPv4 addresses were grouped into classes based
on the first number of the address:

| Class | First octet range | Typical use |
|---|---|---|
| A | 0 – 127 | Very large networks |
| B | 128 – 191 | Medium/large networks |
| C | 192 – 223 | Small networks |
| D | 224 – 239 | Multicast (group communication) |
| E | 240 – 255 | Reserved / experimental |

This classification is exactly what `ip_converter.py` uses in Step 3 of its
workflow.

---

## 2. IPv6 Basics

**IPv6 (Internet Protocol version 6)** is the newer addressing system
designed to replace IPv4. A game-theoretic study of Internet protocols sums
up why it exists in one line: **"Motivated by the exhaustion of the 32-bit
IPv4 addresses, IPv6 provides a 128-bit address space"** (Avramopoulos,
2012).

**Key facts:**

- An IPv6 address is **128 bits** long — four times longer than IPv4.
- It's written as **8 groups of 4 hexadecimal digits, separated by colons**,
  e.g. `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
- Total possible addresses: 2¹²⁸, which a research survey describes as
  **"+340 undecillion (2¹²⁸)"** possible addresses (Hossain, Binti & Uddin,
  2024) — enough that running out is not a realistic concern.
- Long strings of zero groups can be shortened with `::`, but only **once**
  per address (otherwise it would be ambiguous how many zero groups to put
  back).
- An IPv4 address can be embedded inside an IPv6 address using the
  `::ffff:a.b.c.d` convention — this is what `ip_converter.py` uses in
  Step 5 of its workflow.

---

## 3. Why We Need Both

It's natural to ask: if IPv6 is so much bigger, why hasn't it just replaced
IPv4? The research literature gives a few clear reasons.

**1. IPv4 ran out of room.** IPv4's 4.3 billion addresses sounded like a lot
in the 1980s, but is not enough for today's billions of phones, laptops, and
IoT devices. One paper notes IPv6 exists specifically to **"solve the
problem of IPv4 address exhaustion and allow the growth of the Internet"**
(Li & Wong, 2021).

**2. The switch can't happen overnight.** Every router and device on the
Internet would need to support the new protocol, and that takes years. A
study on IPv4/IPv6 coexistence puts it plainly: **"IPv4 and IPv6 coexistence
has been under discussion from the past decade"** (Aazam & Huh, 2014),
because it's **"not practical to change the Internet or any large network
altogether into an IPv6 network at once"**, since all routers can't be
upgraded simultaneously.

**3. The two protocols can't talk to each other directly.** IPv4 and IPv6
packets are structured differently, so a device that only understands one
can't natively reach a device that only understands the other. This is why
tools like `ip_converter.py`, and real transition techniques like dual-stack,
tunneling, and translation, exist — they act as a bridge.

**4. Neither one wins on every metric yet.** A large-scale measurement study
sending test traffic to nearly 1,800 dual-stack websites found that,
compared with IPv4, **"IPv6 has better connectivity, lower packet loss, and
similar hop count"** — but slightly worse latency and throughput in some
cases (Li & Wong, 2021). So for now, supporting both protocols gives the
most reliable overall experience.

**In short:** IPv4 is still everywhere and can't be switched off overnight,
while IPv6 is where the Internet is headed. Software has to understand both
during this (multi-year) transition period.

---

## 4. Simple Examples

### Example 1 — A Class A address

```
Input        : 10.5.5.5
Valid?       : Yes (4 numbers, all 0–255)
Class        : Class A   (first octet 10 is in the range 0–127)
Binary       : 00001010.00000101.00000101.00000101
Back to dec. : 10.5.5.5   (round trip matches)
IPv6 (mixed) : ::ffff:10.5.5.5
```

### Example 2 — A Class C address

```
Input        : 192.0.2.1
Valid?       : Yes
Class        : Class C   (first octet 192 is in the range 192–223)
Binary       : 11000000.00000000.00000010.00000001
Back to dec. : 192.0.2.1   (round trip matches)
IPv6 (mixed) : ::ffff:192.0.2.1
```

### Example 3 — An invalid address

```
Input        : 999.1.1.1
Valid?       : No — 999 is outside the allowed 0–255 range
```

### Example 4 — An IPv6 address, expanded vs. compressed

```
Compressed : 2001:db8::1
Expanded   : 2001:0db8:0000:0000:0000:0000:0000:0001
```

---

## 5. Bonus Questions & Answers

**Q1. Why does an IPv4 octet stop at 255?**
Because each octet is 8 bits, and the largest number you can represent with
8 bits is 2⁸ − 1 = 255. Anything higher wouldn't fit in a single byte.

**Q2. Why is 127.0.0.1 special?**
It's the standard "loopback" address — a computer talking to itself — and it
falls inside the Class A range (0–127), though the whole `127.0.0.0/8` block
is reserved for loopback use rather than being assigned to real hosts.

**Q3. What does the `::` shorthand in IPv6 actually mean?**
It means "however many groups of `0000` are needed to make the address 8
groups long, put them here." It can only be used once per address — if it
were used twice, there'd be no way to know how many zero groups belong to
each `::`.

**Q4. Is Class D or Class E used for normal websites?**
No. Class D (224–239) is reserved for multicast (one sender, many
receivers), and Class E (240–255) is reserved for research/experimental use.
Regular websites and devices use Class A, B, or C addresses.

**Q5. Why does `ip_converter.py` show three different IPv6 formats for the
same address?**
Because IPv6 allows multiple valid text representations of the exact same
128-bit value — a fully expanded form, a compressed form using `::`, and a
"mixed" form that keeps the original IPv4 digits visible at the end. All
three represent identical underlying bits; only the notation differs.

**Q6. Will IPv4 ever completely disappear?**
Not soon. Because so much existing hardware and software is IPv4-only, and
because upgrading everything at once is impractical, research on the
transition period expects IPv4 and IPv6 to keep coexisting for a long time,
with IPv6 gradually taking over as more networks and devices adopt it.

---

## References / Relevant Links

1. Hossain, M. T., Binti, J. Z., & Uddin, M. R. (2024). *A Review Paper on
   IPv4 and IPv6: A Comprehensive Survey.* American Journal of Computer
   Science and Technology, 7(4), 170–175.
   DOI: [10.11648/j.ajcst.20240704.14](https://doi.org/10.11648/j.ajcst.20240704.14)

2. Avramopoulos, I. (2012). *Architectural Innovation: A Game-Theoretic
   Approach.* arXiv preprint.
   [arXiv:1210.7789](https://arxiv.org/abs/1210.7789)

3. Aazam, M., & Huh, E.-N. (2014). *Impact of IPv4-IPv6 Coexistence in Cloud
   Virtualization Environment.* Annals of Telecommunications, 69, 485–496.
   [arXiv:1601.06666](https://arxiv.org/abs/1601.06666)

4. Li, K.-H., & Wong, K.-Y. (2021). *Empirical Analysis of IPv4 and IPv6
   Networks through Dual-Stack Sites.* Information, 12(6), 246.
   DOI: [10.3390/info12060246](https://doi.org/10.3390/info12060246)

---

*This page supports the `ip_converter.py` script in this repository. For
instructions on running the script, see the [README](../README.md).*
