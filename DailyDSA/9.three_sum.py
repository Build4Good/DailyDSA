"""
LeetCode 15: 3Sum
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

The solution set must NOT contain duplicate triplets.

Example:
    nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    list_comp=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        else:
            l=i+1
            r=len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    list_comp.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1


    return list_comp

# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# (order of triplets, and order within each triplet, doesn't matter)
# ─────────────────────────────────────────────

def normalize(result):
    return sorted(sorted(triplet) for triplet in result)


def run_tests():
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),   # classic case, has a duplicate to filter
        ([0, 1, 1], []),                                        # no triplet sums to zero
        ([0, 0, 0], [[0, 0, 0]]),                               # all zeros -- one valid triplet
        ([0, 0, 0, 0], [[0, 0, 0]]),                            # extra zero -- must NOT duplicate the triplet
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),           # multiple valid, non-overlapping triplets
        ([1, 2, -2, -1], []),                                    # only 4 elements, no valid triplet
        ([], []),                                                 # empty array
        ([1, -1], []),                                            # fewer than 3 elements
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = three_sum(nums)
        result_norm = normalize(result) if result else []
        expected_norm = normalize(expected)
        ok = result_norm == expected_norm
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()