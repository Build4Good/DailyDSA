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
    prd_left=[1]*len(nums)
    prd_right=[1]*len(nums)
    current_mul=1
    ## try to create left product table=

    for i in range(1,len(nums)):
        current_mul=current_mul*nums[i-1]
        prd_left[i]=current_mul

    ## try to create right product table
    current_mul=1
    for i in range(len(nums)-2,-1,-1):
        current_mul =current_mul*nums[i+1]
        prd_right[i]=current_mul


    list_prd=[1]*len(nums)
    # return [prd_left*prd_right]  
    for i in range(len(nums)):
        list_prd[i]=prd_left[i]*prd_right[i]

    return list_prd

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