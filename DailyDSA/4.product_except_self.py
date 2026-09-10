"""


Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all elements of nums except
nums[i].

You must write an algorithm that runs in O(n) time and WITHOUT
using the division operation.

Example:
    nums = [1, 2, 3, 4]
    answer = [24, 12, 8, 6]
    (24 = 2*3*4, 12 = 1*3*4, 8 = 1*2*4, 6 = 1*2*3)
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    # TODO: implement your solution here
    pass


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),         # classic case
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),    # a zero in the array
        ([0, 0], [0, 0]),                          # two zeros -- everything becomes 0
        ([2, 3], [3, 2]),                           # smallest real case, no zeros
        ([1, 1, 1, 1], [1, 1, 1, 1]),               # all ones
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),     # all negative
        ([5], [1]),                                  # single element -- product of "everything else" is empty -> 1
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = product_except_self(nums)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()