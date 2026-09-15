"""
LeetCode 11: Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n
vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water. Return the
maximum amount of water a container can store.

Note: you may not slant the container.

Example:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49 (lines at index 1 and index 8: min(8,7) * (8-1) = 49)
"""

from typing import List


def max_area(height: List[int]) -> int:
    max_area_space=0
    l=0
    r=len(height)-1

    while l<r:
        area=(r-l)*min(height[l],height[r])
        max_area_space=max(max_area_space,area)
        if height[r]>height[l]:
            l+=1
        else:
            r-=1    

    return max_area_space
# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),     # classic case
        ([1, 1], 1),                             # smallest possible case
        ([4, 3, 2, 1, 4], 16),                   # tall lines at both ends
        ([1, 2, 1], 2),                          # short-tall-short
        ([1, 2, 4, 3], 4),                       # best pair isn't the two tallest lines
        ([2, 3, 4, 5, 18, 17, 6], 17),           # best pair is NOT at the very ends
        ([1, 1, 1, 1, 1], 4),                    # all equal heights -- widest pair wins
    ]

    passed = 0
    for i, (heights, expected) in enumerate(tests, 1):
        result = max_area(heights)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  height={heights} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()