"""
LeetCode 191: Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Given a positive integer n, return the number of set bits (1s) in its
binary representation (also called the Hamming weight).

Example:
    n = 11   -> binary 1011      -> 3
    n = 128  -> binary 10000000  -> 1

Try both approaches:
    1. Check the last bit with (n & 1), then shift with (n >> 1)
    2. Drop the lowest set bit with n & (n - 1), counting until n == 0
"""


def hamming_weight(n: int) -> int:
    # TODO: implement your solution here
    pass


def run_tests():
    tests = [
        (11, 3),            # 1011
        (128, 1),           # 10000000
        (2147483645, 30),   # 1111111111111111111111111111101
        (1, 1),
        (0, 0),             # no set bits
        (255, 8),           # 11111111
        (1024, 1),          # a single high bit
        (7, 3),             # 111
    ]
    passed = 0
    for i, (n, exp) in enumerate(tests, 1):
        res = hamming_weight(n)
        ok = res == exp
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  n={n} ({bin(n)}) -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()