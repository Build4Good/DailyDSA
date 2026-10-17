"""
REVISION from memory: Merge Intervals (LeetCode 56)

Merge all overlapping intervals and return the result sorted by start.
Touching counts as overlap: [1,4] + [4,5] -> [1,5].
Input is NOT sorted. Don't mutate the input. Target: O(n log n). No notes - 20 minutes.
"""

import random
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # TODO
    interval_c=[intv[:] for intv in sorted(intervals)]
    result=[]
    result.append(interval_c[0]) if interval_c else None

    for i in range(1,len(interval_c)):

        if result[-1][-1]>=interval_c[i][0]:
            ##overlap exists
            result[-1][-1]=max(result[-1][-1],interval_c[i][1])
        else:
            result.append(interval_c[i])    
    return result
def _brute(intervals):
    # paint every covered point, then read the runs back (touching = one run)
    if not intervals:
        return []
    pts = set()
    for s, e in intervals:
        pts.update(x * 2 for x in range(s, e + 1))
        pts.update(x * 2 + 1 for x in range(s, e))
    out, run = [], None
    for p in sorted(pts):
        if run and p == run[1] + 1:
            run[1] = p
        else:
            if run: out.append([run[0] // 2, run[1] // 2])
            run = [p, p]
    out.append([run[0] // 2, run[1] // 2])
    return out


if __name__ == "__main__":
    tests = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([], []),
        ([[5, 7]], [[5, 7]]),
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),
        ([[8, 10], [1, 3], [2, 6]], [[1, 6], [8, 10]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[1, 4], [2, 3], [3, 8], [9, 9]], [[1, 8], [9, 9]]),
        ([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]], [[1, 3], [4, 7]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
    ]
    passed = 0
    for i, (iv, e) in enumerate(tests, 1):
        snapshot = [x[:] for x in iv]
        r = merge(iv)
        ok = r == e and iv == snapshot
        passed += ok
        note = "" if iv == snapshot else "  <- INPUT WAS MUTATED"
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {snapshot} -> {r} (expected {e}){note}")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(3)
    bad = 0
    for _ in range(3000):
        iv = []
        for _ in range(random.randint(0, 8)):
            s = random.randint(0, 25)
            iv.append([s, s + random.randint(0, 6)])
        if merge([x[:] for x in iv]) != _brute(iv):
            bad += 1
            if bad == 1:
                print("First random mismatch:", iv, "expected", _brute(iv))
    print(f"Random check: {3000 - bad}/3000 match brute force")
