"""
BITWISE PRACTICE — Level 1 (P1–P3). Doc section 5.
bit 0 = rightmost bit. Mask for bit i: 1 << i
"""


def is_bit_set(n: int, i: int) -> bool:
    """P1. Is bit i of n equal to 1?   13 = 1101 -> bit 2 is set, bit 1 is not."""
    # TODO
    return ((n>>i)&1)==1


def set_bit(n: int, i: int) -> int:
    """P2a. Turn bit i ON.     13 (1101), i=1 -> 15 (1111)"""

    return n | (1<<i)


def clear_bit(n: int, i: int) -> int:
    """P2b. Turn bit i OFF.    13 (1101), i=2 -> 9 (1001)"""
    # TODO
    return n & ~(1<<i)


def toggle_bit(n: int, i: int) -> int:
    """P2c. Flip bit i.        13 (1101), i=0 -> 12 (1100)"""
    # TODO
    return n ^ (1<<i)


def is_power_of_two(n: int) -> bool:
    """P3. LeetCode 231. One line, no loops. A power of two has exactly one 1 bit.
    Careful with 0 and negatives."""
    # TODO
    return (n>0 and ((n & (n-1))==0))


def run_tests():
    total = passed = 0
    def check(label, got, exp):
        nonlocal total, passed
        total += 1; ok = got == exp; passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {label:<32} got {got!r}, expected {exp!r}")

    check("P1 is_bit_set(13, 2)", is_bit_set(13, 2), True)
    check("P1 is_bit_set(13, 1)", is_bit_set(13, 1), False)
    check("P1 is_bit_set(13, 0)", is_bit_set(13, 0), True)
    check("P1 is_bit_set(8, 3)", is_bit_set(8, 3), True)
    check("P1 is_bit_set(8, 4)", is_bit_set(8, 4), False)
    check("P2 set_bit(13, 1)", set_bit(13, 1), 15)
    check("P2 set_bit(13, 0) (already on)", set_bit(13, 0), 13)
    check("P2 set_bit(0, 4)", set_bit(0, 4), 16)
    check("P2 clear_bit(13, 2)", clear_bit(13, 2), 9)
    check("P2 clear_bit(13, 1) (already off)", clear_bit(13, 1), 13)
    check("P2 clear_bit(15, 0)", clear_bit(15, 0), 14)
    check("P2 toggle_bit(13, 0)", toggle_bit(13, 0), 12)
    check("P2 toggle_bit(13, 1)", toggle_bit(13, 1), 15)
    check("P2 toggle twice = original", toggle_bit(toggle_bit(13, 3), 3), 13)
    for n, e in [(1, True), (2, True), (16, True), (1024, True), (0, False), (6, False), (218, False), (-16, False), (-1, False)]:
        check(f"P3 is_power_of_two({n})", is_power_of_two(n), e)
    print(f"\n{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
