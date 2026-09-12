"""
LeetCode 152: Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous subarray (containing
at least one number) which has the largest product, and return the
product.

Example:
    nums = [2, 3, -2, 4]
    The subarray [2, 3] has the largest product = 6
"""

from typing import List


def max_product(nums: List[int]) -> int:
    current_product=nums[0]
    min_product=nums[0]
    mx_product=nums[0]
    for i in range(1,len(nums)):
        
        mx_product=max(current_product*nums[i],nums[i],min_product*nums[i],mx_product)
        min_product=min(current_product*nums[i],min_product*nums[i])
    return mx_product

# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([2, 3, -2, 4], 6),                # classic case
        ([-2, 0, -1], 0),                   # a zero breaks any subarray spanning it
        ([-2, 3, -4], 24),                  # TWO negatives multiply into a positive -- whole array is best
        ([2, -5, -2, -4, 3], 24),           # non-obvious: best subarray is [-2,-4,3] = 24, not a prefix or suffix
        ([-2], -2),                          # single negative
        ([0, 2], 2),                         # zero then positive
        ([-1, -2, -3, 0], 6),                # negatives before a zero
        ([3, -1, 4], 4),                     # a negative in the middle breaks the run
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = max_product(nums)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()