"""
LeetCode 57: Insert Interval
https://leetcode.com/problems/insert-interval/

You are given `intervals`: non-overlapping intervals, ALREADY SORTED by start.
You are also given one `newInterval`.

Insert newInterval so the result is still sorted and non-overlapping
(merge where needed). Return the new list.

Example:
    intervals = [[1,3],[6,9]], newInterval = [2,5]
    -> [[1,5],[6,9]]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    -> [[1,2],[3,10],[12,16]]

Think in 3 phases while walking left to right:
    1. intervals that end BEFORE newInterval starts  -> copy as-is
    2. intervals that OVERLAP newInterval            -> grow newInterval
    3. intervals that start AFTER newInterval ends   -> copy as-is
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # TODO: implement your solution here
        intervals_c=[iv[:] for iv in intervals]
        result=[]
        interval_exluded=True
        for interval in intervals_c:

            # if newInterval[0]<=interval[-1] and newInterval[0]>=interval[0]:
            #     interval[-1]=max(newInterval[-1],interval[-1])
            #     result.append(interval)
            # elif  newInterval[-1]>=interval[-1]  and newInterval[0]<=interval[0]:
            #     result.append()

            if interval[-1]<newInterval[0]:
                ## the new interval does not overlap existing interval is smaller
                result.append(interval)
            elif interval[0]>newInterval[-1]:
                if interval_exluded:
                    result.append(newInterval)
                    interval_exluded=False
                ## the new interval does not overlap the interval starting is already bigger than the new interval higher end
                result.append(interval)
            else:
                newInterval=[min(interval[0],newInterval[0]),max(interval[-1],newInterval[-1])]
        if interval_exluded:
            result.append(newInterval)        

        return result        
# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),                                   # classic
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),  # swallows several
        ([], [5, 7], [[5, 7]]),                                                         # empty input
        ([[1, 5]], [2, 3], [[1, 5]]),                                                   # new one fully inside
        ([[3, 5]], [1, 2], [[1, 2], [3, 5]]),                                           # goes at the very start
        ([[1, 2]], [4, 6], [[1, 2], [4, 6]]),                                           # goes at the very end
        ([[1, 2], [6, 7]], [3, 4], [[1, 2], [3, 4], [6, 7]]),                           # fits in a gap, no merge
        ([[1, 5]], [5, 7], [[1, 7]]),                                                   # touching ends merge
        ([[2, 3], [5, 6]], [1, 10], [[1, 10]]), 
        ([[1, 2], [6, 7], [9, 10]], [3, 4], [[1, 2], [3, 4], [6, 7], [9, 10]]),                                           # new one swallows everything
    ]

    sol = Solution()
    passed = 0
    for i, (intervals, new, expected) in enumerate(tests, 1):
        result = sol.insert([iv[:] for iv in intervals], new[:])
        ok = result == expected
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {intervals} + {new} -> {result} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")