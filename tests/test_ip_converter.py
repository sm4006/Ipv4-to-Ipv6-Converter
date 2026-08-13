"""
Automated tests for ip_converter.py

Run with:
    pytest -v
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ip_converter import (  # noqa: E402
    is_valid_ipv4,
    classify_ipv4,
    dotted_decimal_to_binary,
    dotted_binary_to_decimal,
    ipv4_to_ipv6_formats,
)


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def test_valid_addresses():
    assert is_valid_ipv4("192.0.2.1") is True
    assert is_valid_ipv4("0.0.0.0") is True
    assert is_valid_ipv4("255.255.255.255") is True
    assert is_valid_ipv4("10.5.5.5") is True


def test_invalid_wrong_field_count():
    assert is_valid_ipv4("192.168.1") is False
    assert is_valid_ipv4("192.168.1.1.1") is False


def test_invalid_out_of_range():
    assert is_valid_ipv4("999.1.1.1") is False
    assert is_valid_ipv4("256.0.0.0") is False
    assert is_valid_ipv4("1.2.3.256") is False


def test_invalid_non_numeric():
    assert is_valid_ipv4("a.b.c.d") is False
    assert is_valid_ipv4("192.168.1.x") is False


def test_invalid_leading_zero():
    assert is_valid_ipv4("192.168.01.1") is False


def test_invalid_empty_and_malformed():
    assert is_valid_ipv4("") is False
    assert is_valid_ipv4("...") is False
    assert is_valid_ipv4("192..1.1") is False


# --------------------------------------------------------------------------
# Classification
# --------------------------------------------------------------------------

def test_classify_class_a():
    assert classify_ipv4("10.5.5.5") == "Class A"
    assert classify_ipv4("0.0.0.0") == "Class A"
    assert classify_ipv4("127.0.0.1") == "Class A"


def test_classify_class_b():
    assert classify_ipv4("172.16.0.5") == "Class B"
    assert classify_ipv4("128.0.0.1") == "Class B"
    assert classify_ipv4("191.255.255.255") == "Class B"


def test_classify_class_c():
    assert classify_ipv4("192.0.2.1") == "Class C"
    assert classify_ipv4("223.255.255.255") == "Class C"


def test_classify_class_d():
    assert classify_ipv4("224.0.0.1") == "Class D (Multicast)"
    assert classify_ipv4("239.255.255.255") == "Class D (Multicast)"


def test_classify_class_e():
    assert classify_ipv4("240.0.0.1") == "Class E (Reserved/Experimental)"
    assert classify_ipv4("255.255.255.255") == "Class E (Reserved/Experimental)"


# --------------------------------------------------------------------------
# Binary round trip
# --------------------------------------------------------------------------

def test_decimal_to_binary():
    assert dotted_decimal_to_binary("192.0.2.1") == (
        "11000000.00000000.00000010.00000001"
    )


def test_binary_round_trip():
    for address in ["192.0.2.1", "10.5.5.5", "255.255.255.255", "0.0.0.0"]:
        binary = dotted_decimal_to_binary(address)
        assert dotted_binary_to_decimal(binary) == address


# --------------------------------------------------------------------------
# IPv4 -> IPv6 formats
# --------------------------------------------------------------------------

def test_ipv4_to_ipv6_formats():
    formats = ipv4_to_ipv6_formats("192.0.2.1")
    assert formats["expanded"] == "0000:0000:0000:0000:0000:ffff:c000:0201"
    assert formats["compressed"] == "::ffff:c000:201"
    assert formats["mixed"] == "::ffff:192.0.2.1"


def test_ipv4_to_ipv6_formats_all_represent_same_value():
    formats = ipv4_to_ipv6_formats("10.5.5.5")
    # Expanded form should always contain exactly 8 groups
    assert len(formats["expanded"].split(":")) == 8
    # Mixed form should retain the original dotted-decimal address
    assert formats["mixed"].endswith("10.5.5.5")
