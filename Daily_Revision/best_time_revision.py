"""
LADDER 1/4 (sliding window) - REVISION from memory: Best Time to Buy and Sell Stock (LeetCode 121)

prices[i] is the price on day i. Buy on one day, sell on a LATER day.
Return the max profit; 0 if no profit is possible.
Target: O(n) time, O(1) space. 10-15 minutes.
"""

import random
from typing import List


def max_profit(prices: List[int]) -> int:
    # TODO
    res=0
    
    l=0
    r=1

    while r < len(prices):
        res=max(res,prices[r]-prices[l])

        if prices[l]>prices[r]:
            l=r
        r+=1    
    return res

def _brute(prices):
    return max((prices[j] - prices[i] for i in range(len(prices)) for j in range(i + 1, len(prices))), default=0) if prices else 0


if __name__ == "__main__":
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([], 0),
        ([5], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([3, 3, 3], 0),
        ([2, 4, 1, 7], 6),
        ([2, 10, 1, 5], 8),
        ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 8),
    ]
    passed = 0
    for i, (p, e) in enumerate(tests, 1):
        r = max_profit(p[:])
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {p} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(3)
    bad = 0
    for _ in range(3000):
        p = [random.randint(0, 30) for _ in range(random.randint(0, 12))]
        if max(0, max_profit(p[:])) != max(0, _brute(p)) or max_profit(p[:]) != max(0, _brute(p)):
            bad += 1
            if bad == 1:
                print("First random mismatch:", p, "expected", max(0, _brute(p)))
    print(f"Random check: {3000 - bad}/3000 match brute force")
