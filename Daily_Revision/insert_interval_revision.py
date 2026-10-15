"""
REVISION from memory: Insert Interval (LeetCode 57)

intervals: sorted by start, non-overlapping. Insert new_interval and merge
where needed. Return the resulting sorted, non-overlapping list.
Touching counts as overlap: [1,2] + [2,3] -> [1,3].
Target: O(n). Don't mutate the input. No notes - 20 minutes.
"""

import random
from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # TODO
    interval_c = [ intv[:] for intv in intervals]
    result=[]
    merge_result=[]
    interval_added=False
    for start,end in interval_c:

        if end>=new_interval[0] and interval_added is False:
            if start>new_interval[0]:
                result.append(new_interval)
                result.append([start,end])
            else:
                result.append([min(start,new_interval[0]),max(end,new_interval[1])])
            interval_added=True
        else:    
            result.append([start,end])
    if interval_added is False :
        result.append(new_interval)
    merge_result.append(result[0])

    for i in range(1,len(result)):

        if merge_result[-1][1]>=result[i][0]:
            merge_result[-1]=[min(merge_result[-1][0],result[i][0]),max(merge_result[-1][1],result[i][1])]            
        else:
            merge_result.append(result[i])

    return merge_result

def _brute(intervals, new):
    allv = sorted([iv[:] for iv in intervals] + [new[:]])
    out = []
    for s, e in allv:
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


if __name__ == "__main__":
    tests = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        ([[3, 5]], [1, 2], [[1, 2], [3, 5]]),
        ([[1, 2], [3, 4]], [2, 3], [[1, 4]]),
        ([[1, 2], [6, 7], [9, 10]], [3, 4], [[1, 2], [3, 4], [6, 7], [9, 10]]),
        ([[1, 2], [3, 4], [5, 6]], [0, 10], [[0, 10]]),
        ([[1, 5], [10, 12]], [5, 10], [[1, 12]]),
    ]
    passed = 0
    for i, (iv, new, e) in enumerate(tests, 1):
        snapshot = [x[:] for x in iv]
        r = insert(iv, new[:])
        ok = r == e and iv == snapshot
        passed += ok
        note = "" if iv == snapshot else "  <- INPUT WAS MUTATED"
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {snapshot} + {new} -> {r} (expected {e}){note}")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(11)
    bad = 0
    for _ in range(3000):
        base = _brute([[s, s + random.randint(0, 4)] for s in random.sample(range(0, 40), random.randint(0, 7))], [100, 100])[:-1]
        s = random.randint(0, 45)
        new = [s, s + random.randint(0, 10)]
        if insert([x[:] for x in base], new[:]) != _brute(base, new):
            bad += 1
            if bad == 1:
                print("First random mismatch:", base, new, "expected", _brute(base, new))
    print(f"Random check: {3000 - bad}/3000 match brute force")
