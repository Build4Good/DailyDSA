"""


You are given an array `prices` where prices[i] is the price of a
given stock on day i.

You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day IN THE FUTURE to sell that
stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example:
    prices = [7, 1 , 5, 3, 6, 4]
    Buy on day 2 (price = 1), sell on day 5 (price = 6),
    profit = 6 - 1 = 5
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    # TODO: implement your solution here
    left=0
    right=1
    max_profit=0

    while right<len(prices):

        if prices[left]>prices[right]:
            left+=1
            right=left+1
        else:
            max_profit= max(max_profit,prices[right]-prices[left])
            right+=1

    return max_profit            

    


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),      # classic case
        ([7, 6, 4, 3, 1], 0),          # strictly decreasing -- no profit possible
        ([1, 2], 1),                    # smallest possible profitable case
        ([2, 1], 0),                    # smallest possible no-profit case
        ([3, 3, 3, 3], 0),               # flat prices -- no profit
        ([2, 4, 1, 7], 6),               # min isn't at index 0; max isn't at the end
        ([1], 0),                        # single price, no transaction possible
    ]

    passed = 0
    for i, (prices, expected) in enumerate(tests, 1):
        result = max_profit(prices)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  prices={prices} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()