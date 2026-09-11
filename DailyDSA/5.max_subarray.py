"""
LeetCode 53: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum, and return that sum.

Example:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    The subarray [4, -1, 2, 1] has the largest sum = 6
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    # TODO: implement your solution here
    max_sum=nums[0]
    total_max=nums[0]

    for i in range(1,len(nums)):
        max_sum=max(nums[i],max_sum+nums[i])
        total_max=max(max_sum,total_max)

    return total_max


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),    # classic case
        ([1], 1),                                  # single element
        ([5, 4, -1, 7, 8], 23),                    # all positive-leaning, whole array is best
        ([-1], -1),                                 # single negative -- must still return it
        ([-3, -2, -1, -4], -1),                     # ALL negative -- best is the least-negative single element
        ([0, 0, 0, 0], 0),                          # all zeros
        ([-2, -1], -1),                             # two negatives, best is the larger (less negative) one
        ([8, -19, 5, -4, 20], 21),                  # non-obvious: best subarray is [5, -4, 20], not the whole array
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = max_subarray(nums)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()