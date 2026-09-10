
"""
LeetCode 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears
at least twice in the array, and False if every element is distinct.
"""

from typing import List


def find_duplicate(elements: List[int]) -> bool:
    dict_ele={}
    for num in elements:
        if num in dict_ele:
            return True
        else :
            dict_ele[num]=dict_ele.get(num,0)+1

    return False        

# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([1, 2, 3, 1], True),          # classic case, duplicate present
        ([1, 2, 3, 4], False),          # all distinct
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),   # multiple duplicates
        ([], False),                     # empty array
        ([1], False),                    # single element
        ([1, 1, 1, 1], True),            # all identical
        ([-1, -2, -3, -1], True),        # negative numbers, duplicate
        ([-1, -2, -3, -4], False),       # negative numbers, no duplicate
        ([0, 0], True),                  # zeros, duplicate
        ([0, 1, 2], False),              # zero present, no duplicate
        (list(range(10000)) + [9999], True),  # large array, duplicate at the very end
    ]

    passed = 0
    for i, (nums, expected) in enumerate(tests, 1):
        result = find_duplicate(nums)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        display_nums = nums if len(nums) <= 15 else f"[large array, {len(nums)} elements]"
        print(f"Test {i}: {status}  nums={display_nums} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()