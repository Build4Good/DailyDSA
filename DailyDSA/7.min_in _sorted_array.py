"""
LeetCode 153: Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n, sorted in ascending order, is rotated
between 1 and n times. Given the rotated array nums of UNIQUE
elements, return the minimum element.

You must write an algorithm that runs in O(log n) time.

Example:
    nums = [4, 5, 6, 7, 0, 1, 2]  (originally [0,1,2,4,5,6,7], rotated)
    minimum = 0
"""

from typing import List
import math

def find_min(nums: List[int]) -> int:
    # TODO: implement your solution here
    l=0
    r=len(nums)-1
    if len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        if nums[0]<nums[1]:
            return nums[0]
        else:
            return nums[1]
    else:        
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                #### left side already sorted
                l=mid+1
            else:
                r=mid


    return nums[l]


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0),      # classic case, pivot in the middle
        ([3, 4, 5, 1, 2], 1),             # pivot earlier
        ([11, 13, 15, 17], 11),            # NOT rotated at all -- already fully sorted
        ([1], 1),                          # single element
        ([2, 1], 1),                       # smallest possible rotated case
        ([5, 1, 2, 3, 4], 1),              # pivot right after the first element
        ([1, 2, 3, 4, 5], 1),              # not rotated, ascending, min is first element
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = find_min(nums)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()