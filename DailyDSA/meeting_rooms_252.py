"""
Meeting Rooms (LeetCode 252 - premium; free version: NeetCode "Meeting Schedule")
https://neetcode.io/problems/meeting-schedule

Given meeting time intervals [[start, end], ...], return True if ONE person
can attend ALL meetings (i.e. no two meetings overlap).

Touching is fine: [1,2] and [2,3] do NOT overlap (one ends as the next starts).

Example:
    [[0,30],[5,10],[15,20]]  -> False   ([0,30] overlaps the others)
    [[7,10],[2,4]]           -> True

Target: O(n log n). You've done the hard version of this already (435).
"""

from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    # TODO
    intervals_up=[intv[:] for intv in sorted(intervals)]

    for i in range(1,len(intervals_up)):

        if intervals_up[i-1][1]>intervals_up[i][0]:
            return False 

    return True
if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], False),   # classic overlap
        ([[7, 10], [2, 4]], True),               # unsorted, no overlap
        ([], True),                              # no meetings
        ([[5, 8]], True),                        # single meeting
        ([[1, 2], [2, 3], [3, 4]], True),        # touching is fine
        ([[1, 5], [2, 3]], False),               # one inside another
        ([[9, 10], [1, 3], [4, 9]], True),       # unsorted, touching
        ([[1, 3], [6, 8], [2, 4]], False),       # overlap hidden until sorted
    ]
    passed = 0
    for i, (iv, e) in enumerate(tests, 1):
        r = can_attend_meetings([x[:] for x in iv])
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {iv} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")
