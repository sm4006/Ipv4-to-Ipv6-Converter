#!/usr/bin/env python3
"""
ip_converter.py
================

Interactive IPv4 address checker, classifier, and IPv6 converter.

Workflow (matches the project spec exactly):
    1. Read an IP address from the user.
    2. Check the validity of the IP address:
         a. It must have 4 dotted numbers (A.B.C.D)
         b. Each of A, B, C, D must lie between 0 and 255
    3. If valid, classify the address into Class A, B, C, D (or E).
    4. Convert the valid dotted-decimal address into dotted-binary,
       then convert that binary form back into dotted-decimal
       (round-trip check).
    5. Convert the IPv4 address into an IPv6 address and display it
       in three different formats.

Run it directly for an interactive prompt:
    python3 ip_converter.py

Background reading (address structure, why IPv4 and IPv6 both exist,
worked examples, and bonus Q&A) lives in the project Wiki page
"IPv4-IPv6-Basics-and-Examples.md".
"""

from __future__ import annotations


# --------------------------------------------------------------------------
# Step 2: Validation
# --------------------------------------------------------------------------

def is_valid_ipv4(address: str) -> bool:
    """
    Check that `address` has exactly 4 dot-separated numbers (A.B.C.D)
    and that each number is an integer between 0 and 255 inclusive.
    """
    parts = address.strip().split(".")

    # 2a. Must have exactly 4 dotted numbers
    if len(parts) != 4:
        return False

    for part in parts:
        # Must be a non-empty string of digits only
        if not part.isdigit():
            return False
        # Reject inputs like "01" or "007" (non-canonical leading zeros)
        if len(part) > 1 and part[0] == "0":
            return False
        # 2b. Each value must lie between 0 and 255
        value = int(part)
        if not (0 <= value <= 255):
            return False

    return True


# --------------------------------------------------------------------------
# Step 3: Classification into Class A / B / C / D / E
# --------------------------------------------------------------------------

def classify_ipv4(address: str) -> str:
    """
    Classify a valid IPv4 address into Class A, B, C, D, or E,
    based on the value of the first octet.

        Class A : 0   - 127   (default mask 255.0.0.0)
        Class B : 128 - 191   (default mask 255.255.0.0)
        Class C : 192 - 223   (default mask 255.255.255.0)
        Class D : 224 - 239   (Multicast)
        Class E : 240 - 255   (Reserved / Experimental)
    """
    first_octet = int(address.split(".")[0])

    if 0 <= first_octet <= 127:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    else:  # 240 - 255
        return "Class E (Reserved/Experimental)"


# --------------------------------------------------------------------------
# Step 4: Dotted-decimal -> dotted-binary -> dotted-decimal (round trip)
# --------------------------------------------------------------------------

def dotted_decimal_to_binary(address: str) -> str:
    """Convert a dotted-decimal IPv4 address into dotted 8-bit binary groups."""
    octets = address.split(".")
    return ".".join(f"{int(octet):08b}" for octet in octets)


def dotted_binary_to_decimal(binary_address: str) -> str:
    """Convert a dotted 8-bit binary IPv4 address back into dotted-decimal."""
    groups = binary_address.split(".")
    return ".".join(str(int(group, 2)) for group in groups)


# --------------------------------------------------------------------------
# Step 5: IPv4 -> IPv6, shown in three different formats
# --------------------------------------------------------------------------

def ipv4_to_ipv6_formats(address: str) -> dict:
    """
    Convert a valid IPv4 address into its IPv6-mapped equivalent and
    return it in three different, commonly used formats:

        1. Full/expanded hextet form  -> 0000:0000:0000:0000:0000:ffff:c000:0201
        2. Compressed hextet form     -> ::ffff:c000:201
        3. Mixed (dotted-quad) form   -> ::ffff:192.0.2.1

    All three represent the same IPv4-mapped IPv6 address, per the
    ::ffff:a.b.c.d convention used to embed an IPv4 address inside IPv6.
    """
    octets = [int(o) for o in address.split(".")]

    # Combine the 4 octets into two 16-bit hex groups
    high_word = (octets[0] << 8) | octets[1]
    low_word = (octets[2] << 8) | octets[3]

    # Format 1: fully expanded, all 8 groups shown, no "::"
    expanded = f"0000:0000:0000:0000:0000:ffff:{high_word:04x}:{low_word:04x}"

    # Format 2: compressed hextet form, leading zero groups collapsed to "::"
    compressed = f"::ffff:{high_word:x}:{low_word:x}"

    # Format 3: mixed notation, keeping the trailing IPv4 dotted-quad
    mixed = f"::ffff:{address}"

    return {
        "expanded": expanded,
        "compressed": compressed,
        "mixed": mixed,
    }


# --------------------------------------------------------------------------
# Main interactive program
# --------------------------------------------------------------------------

def main() -> None:
    # Step 1: Read an IP address from the user
    address = input("Enter an IPv4 address (A.B.C.D): ").strip()

    # Step 2: Validate
    if not is_valid_ipv4(address):
        print(f"\n'{address}' is NOT a valid IPv4 address.")
        print("An address must have 4 dotted numbers, each between 0 and 255.")
        return

    print(f"\n'{address}' is a valid IPv4 address.")

    # Step 3: Classify
    ip_class = classify_ipv4(address)
    print(f"Class            : {ip_class}")

    # Step 4: Decimal -> binary -> decimal round trip
    binary_form = dotted_decimal_to_binary(address)
    back_to_decimal = dotted_binary_to_decimal(binary_form)
    print(f"Dotted Binary    : {binary_form}")
    print(f"Back to Decimal  : {back_to_decimal}")
    print(f"Round-trip check : {'OK' if back_to_decimal == address else 'MISMATCH'}")

    # Step 5: IPv4 -> IPv6, three formats
    ipv6_forms = ipv4_to_ipv6_formats(address)
    print("\nIPv4-mapped IPv6 address:")
    print(f"  1. Expanded form   : {ipv6_forms['expanded']}")
    print(f"  2. Compressed form : {ipv6_forms['compressed']}")
    print(f"  3. Mixed form      : {ipv6_forms['mixed']}")


if __name__ == "__main__":
    main()
