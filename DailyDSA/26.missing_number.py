"""
LeetCode 268: Missing Number
nums holds n distinct numbers from the range [0, n]; exactly one is missing.
Return it in O(n) time and O(1) extra space.
Bitwise idea: x ^ x = 0 and x ^ 0 = x. XOR every index 0..n with every value --
everything pairs up and cancels except the missing number.
"""
from typing import List


def missing_number(nums: List[int]) -> int:
    # TODO
    pass


def run_tests():
    tests = [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
             ([0], 1), ([1], 0), ([1, 2], 0)]
    passed = 0
    for i, (nums, exp) in enumerate(tests, 1):
        res = missing_number(list(nums)); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  nums={nums} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()