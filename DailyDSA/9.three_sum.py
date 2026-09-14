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
    dict_complement={}
    list_comp=[]
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            continue
        else:
            target= nums[i]*-1
            for j in range(i+1,len(nums)-1):
                if nums[j]==nums[j+1]:
                    continue
                else:
                    complement = target - nums[j]

                    if complement in dict_complement:
                        list_comp.append([dict_complement[complement],nums[j]])
                    else:
                        dict_complement.setdefault(-complement,[]).append([nums[i],nums[j]])
                       #since get empty list and add indices of those
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