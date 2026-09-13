"""
LeetCode 33: Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with
distinct values), rotated at an unknown pivot. Given the array
nums after the rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity.

Example:
    nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    l=0
    r = len(nums)-1

    while l<r:
        mid=(l+r)//2
        
        if nums[mid]>nums[r]:
            ### left side is sorted,now lest check where the number is if its in left side or right side
            if target>=nums[l] and target <=nums[mid]:
                ### target is in sorted half , since r can be equal to mid r = mid  
                r=mid
            else:
                ### target is not ins orted half
                l=mid+1
        else:
            #### right side is sorted ,now check where the number is is it in right side of mid or left side 
            if target>nums[mid] and target <=nums[r]:
                            ### target is in sorted half
                l=mid+1
            else:
                            ### target is not ins orted half and also not equal to mid so r can be till mid -1 
                r=mid

    return  l if target in nums else -1      


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),      # classic case, target in the "dropped" half
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),       # target in the "sorted-looking" left half
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),      # target genuinely not present
        ([1], 0, -1),                          # single element, not found
        ([1], 1, 0),                           # single element, found
        ([5, 1, 3], 5, 0),                     # target is the first element (the pivot itself)
        ([3, 1], 1, 1),                        # smallest rotated case
        ([1, 2, 3, 4, 5], 3, 2),               # not rotated at all
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(tests, 1):
        result = search(nums, target)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums}, target={target} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()