"""
Meeting Rooms II (LeetCode 253 - premium; free version: NeetCode "Meeting Schedule II")
https://neetcode.io/problems/meeting-schedule-ii

Given meeting intervals [[start, end], ...], return the MINIMUM number of
rooms needed so every meeting gets a room.

Touching is fine: a meeting ending at 10 frees its room for one starting at 10.

Example:
    [[0,30],[5,10],[15,20]] -> 2
    [[7,10],[2,4]]          -> 1

Yesterday you answered "is there ANY overlap?". Today: "what is the MOST
meetings running at the same moment?"  Target: O(n log n).
Hint: you need to know which ongoing meeting ends FIRST.
"""

from typing import List
import heapq



def min_meeting_rooms(intervals: List[List[int]]) -> int:
    # TODO
    h=[]

    intervals_up=sorted(intervals)

    for intv in intervals_up:

        if not h:
            heapq.heappush(h,intv[1])
        else:

            if intv[0]>=h[0]:
                heapq.heappop(h)
                heapq.heappush(h,intv[1])
            else:
                heapq.heappush(h,intv[1])

    return len(h)



if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),           # classic
        ([[7, 10], [2, 4]], 1),                      # no overlap
        ([], 0),                                     # no meetings
        ([[1, 5]], 1),                               # single
        ([[1, 2], [2, 3], [3, 4]], 1),               # touching reuses the room
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 4),      # all nested
        ([[1, 4], [2, 5], [7, 9], [8, 10]], 2),      # two separate clusters
        ([[9, 10], [4, 9], [4, 17]], 2),             # unsorted, touching at 9
        ([[1, 3], [1, 3], [1, 3]], 3),               # identical meetings
    ]
    passed = 0
    for i, (iv, e) in enumerate(tests, 1):
        r = min_meeting_rooms([x[:] for x in iv])
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {iv} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")