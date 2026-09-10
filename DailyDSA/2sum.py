"""

Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers such that they add up to `target`.

Assumptions:
- Exactly one solution exists.
- You may not use the same element twice.
- Return the indices in any order.

Example:
    nums = [2, 7, 11, 15], target = 9
    Because nums[0] + nums[1] == 9, return [0, 1]
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_complement={}

    for i in range (0,len(nums)):
        complement=target-nums[i]

        if complement in dict_complement:
            return [dict_complement[complement],i]
        else:
            dict_complement[nums[i]]=i

    


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        # (nums, target, expected_indices_as_a_SET_of_valid_answers)
        ([2, 7, 11, 15], 9, {(0, 1)}),
        ([3, 2, 4], 6, {(1, 2)}),
        ([3, 3], 6, {(0, 1)}),
        ([1, 2, 3, 4, 5], 9, {(3, 4)}),
        ([-1, -2, -3, -4, -5], -8, {(2, 4)}),
        ([0, 4, 3, 0], 0, {(0, 3)}),
    ]

    passed = 0
    for i, (nums, target, valid_answers) in enumerate(tests, 1):
        result = two_sum(nums, target)
        # Order doesn't matter, but the PAIR of indices must be correct
        result_tuple = tuple(sorted(result)) if result else None
        ok = result_tuple in valid_answers
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  nums={nums}, target={target} -> got {result}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()