"""
REVISION from memory: Non-overlapping Intervals (LeetCode 435)

Return the MINIMUM number of intervals to remove so the rest don't overlap.
Touching is fine: [1,2] and [2,3] do NOT overlap.
Target: O(n log n). No notes - 20 minutes.
"""

import random
from itertools import combinations
from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    # TODO
    interval_c= [intv[:] for intv in sorted(intervals,key=lambda x:x[1])]
    

    overlap_count=0
    valid_end=interval_c[0][-1] if interval_c else None
    
    for i in range (1,len(interval_c)):
        if valid_end>interval_c[i][0]:
            #overlap
            overlap_count+=1
        else:
            valid_end=interval_c[i][1]     

    return overlap_count

def _brute(intervals):
    # try keeping the largest subset that doesn't overlap
    n = len(intervals)
    for keep in range(n, -1, -1):
        for combo in combinations(sorted(intervals), keep):
            if all(combo[i][1] <= combo[i + 1][0] for i in range(len(combo) - 1)):
                return n - keep
    return 0


if __name__ == "__main__":
    tests = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([], 0),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        ([[1, 10], [2, 3], [4, 5], [6, 7]], 1),
        ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
        ([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]], 7),
        ([[5, 6]], 0),
    ]
    passed = 0
    for i, (iv, e) in enumerate(tests, 1):
        r = erase_overlap_intervals([x[:] for x in iv])
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {iv} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(5)
    bad = 0
    for _ in range(1500):
        iv = []
        for _ in range(random.randint(0, 7)):
            s = random.randint(0, 15)
            iv.append([s, s + random.randint(1, 6)])
        if erase_overlap_intervals([x[:] for x in iv]) != _brute(iv):
            bad += 1
            if bad == 1:
                print("First random mismatch:", iv, "expected", _brute(iv))
    print(f"Random check: {1500 - bad}/1500 match brute force")
