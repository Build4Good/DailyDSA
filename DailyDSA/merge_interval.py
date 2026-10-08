"""
LeetCode 56: Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return the non-overlapping intervals
that cover all the intervals in the input.

Example:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    -> [[1,6],[8,10],[15,18]]     ([1,3] and [2,6] overlap)

Note: [1,4] and [4,5] count as overlapping -> [1,5]
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TODO: implement your solution here
        interval_copy = sorted(iv[:] for iv in intervals)

        
        result=[]
        result.append(interval_copy[0])

        for index in range(1,len(interval_copy)):
            if interval_copy[index][0]<=result[-1][1]:
                result[-1][1]=max(interval_copy[index][-1],result[-1][1])
                
            else:
                result.append(interval_copy[index])
                  
        return result

# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),  # classic
        ([[1, 4], [4, 5]], [[1, 5]]),                                        # touching ends count as overlap
        ([[1, 4]], [[1, 4]]),                                                # single interval
        ([[4, 7], [1, 4]], [[1, 7]]),                                        # input NOT sorted
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),                              # one interval swallows others
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),                # no overlaps at all
        ([[2, 3], [1, 2], [5, 8], [6, 7], [0, 0]], [[0, 0], [1, 3], [5, 8]]),# mixed, unsorted, contained
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),                                # zero-length interval
    ]

    sol = Solution()
    passed = 0
    for i, (intervals, expected) in enumerate(tests, 1):
        result = sol.merge([iv[:] for iv in intervals])  # pass a copy
        ok = result is not None and sorted(result) == sorted(expected)
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {intervals} -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")