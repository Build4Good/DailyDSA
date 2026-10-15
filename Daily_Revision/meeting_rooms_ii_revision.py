"""
REVISION from memory: Meeting Rooms II (LeetCode 253 / NeetCode "Meeting Schedule II")

Return the MINIMUM number of rooms so every meeting gets one.
Touching is fine: a meeting ending at 10 frees its room for one starting at 10.
Target: O(n log n). No notes, no hints - 20 minutes.
"""

import heapq
import random
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    # TODO
    h=[]

    for start,end in sorted(intervals):

        if  h and h[0]<=start:
            heapq.heappop(h)

        heapq.heappush(h, end)

    return len(h)        


def _brute(intervals):
    # count meetings running at each start time (half-open [start, end))
    return max((sum(s <= t < e for s, e in intervals) for t, _ in intervals), default=0)


if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([], 0),
        ([[1, 5]], 1),
        ([[1, 2], [2, 3], [3, 4]], 1),
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 4),
        ([[1, 4], [2, 5], [7, 9], [8, 10]], 2),
        ([[9, 10], [4, 9], [4, 17]], 2),
        ([[1, 3], [1, 3], [1, 3]], 3),
        ([[1, 5], [5, 10], [2, 3]], 2),
        ([[0, 5], [1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ]
    passed = 0
    for i, (iv, e) in enumerate(tests, 1):
        r = min_meeting_rooms([x[:] for x in iv])
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {iv} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(7)
    bad = 0
    for _ in range(3000):
        iv = []
        for _ in range(random.randint(0, 8)):
            s = random.randint(0, 20)
            iv.append([s, s + random.randint(1, 8)])
        if min_meeting_rooms([x[:] for x in iv]) != _brute(iv):
            bad += 1
            if bad == 1:
                print("First random mismatch:", iv, "expected", _brute(iv))
    print(f"Random check: {3000 - bad}/3000 match brute force")
