"""
REVISION — LeetCode 33: Search in Rotated Sorted Array
Return the index of target in a rotated sorted array of distinct values,
or -1. Must be O(log n).
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    # TODO: from memory
    l=0
    r=len(nums)-1
    while l<r:
        mid=(l+r)//2

        if nums[mid]> nums[r]:
            ### left side is sorted ,rotation in second half
            if target>=nums[l] and target <=nums[mid]:
                ###target is within this half, move r to the first half endpoint
                r=mid
            else:

                l=mid+1
        else:
            ### right side is sorted 
            if target>nums[mid] and target <=nums[r]:
                l=mid+1
            else:
                r= mid   
    
    return l if nums[l]==target else -1

def run_tests():
    tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1), ([1], 0, -1), ([1], 1, 0),
        ([5, 1, 3], 5, 0), ([3, 1], 1, 1), ([1, 2, 3, 4, 5], 3, 2),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0), ([4, 5, 6, 7, 0, 1, 2], 2, 6),
    ]
    passed = 0
    for i, (nums, t, exp) in enumerate(tests, 1):
        res = search(nums, t)
        ok = res == exp
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  nums={nums}, target={t} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()