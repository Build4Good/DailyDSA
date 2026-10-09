"""
LeetCode 435: Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals, return the MINIMUM number of intervals
you need to REMOVE so the rest do not overlap.

NOTE the difference from 56/57: here touching ends do NOT overlap.
    [1,2] and [2,3]  -> fine, no overlap

Example:
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    -> 1     (remove [1,3]; the rest only touch)

Hint: think "keep as many as possible". Which interval should you keep
when two overlap - the one that ends early, or the one that ends late?
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # TODO: implement your solution here
        intervals_up = sorted(intervals)

        previous_interval_high=intervals_up[0][-1]
        count=0
        for i in range(1,len(intervals_up)):

            if intervals_up[i][0]<previous_interval_high:
                count+=1
                
            else:
                previous_interval_high=intervals_up[i][1]    

        return min(count,len(intervals_up)-count)
# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),            # classic
        ([[1, 2], [1, 2], [1, 2]], 2),                    # duplicates: keep one
        ([[1, 2], [2, 3]], 0),                            # touching is NOT overlapping
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),      # one long interval blocks many
        ([[5, 6]], 0),                                    # single interval
        ([[1, 5], [2, 3], [3, 4]], 1),                    # remove the long one, not the short ones
        ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),    # chain of overlaps
        ([[-5, -1], [-3, 0], [0, 3]], 1),                 # negatives
    ]

    sol = Solution()
    passed = 0
    for i, (intervals, expected) in enumerate(tests, 1):
        result = sol.eraseOverlapIntervals([iv[:] for iv in intervals])
        ok = result == expected
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {intervals} -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")