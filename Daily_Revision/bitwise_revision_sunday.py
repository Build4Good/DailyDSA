"""
REVISION from memory - two bitwise problems (from your Oct 4-7 bitwise set). 20 minutes each, no notes.

P1. Single Number III (LeetCode 260)
    Every number appears exactly twice except TWO numbers, which appear once.
    Return those two (any order - the tests sort them). Target: O(n) time, O(1) extra space.

P2. Bitwise AND of Numbers Range (LeetCode 201)
    Given 0 <= left <= right, return left & (left+1) & ... & right.
    Target: O(log right) - do NOT loop over the whole range.
"""

import random
from functools import reduce
from typing import List


def single_number_iii(nums: List[int]) -> List[int]:
    # TODO
    c=0
    a=0
    b=0
    for num in nums:
        c^=num
    ### c will only have a^b two numbeer which dont cancel out each other 
    mask = c &(-c)   ### we take the lowest set bit , we will only have one bit set, XOR is only 1 if they differ so one of them would be one other goes to zero

    for num in nums:

        if (num & mask)==0:
            a^=num
        else:
            b^=num    

    return [a,b]



def range_bitwise_and(left: int, right: int) -> int:
    # TODO
    number_of_shifts=0

    while(left<right):
        left=left>>1
        right=right>>1
        number_of_shifts+=1

    return right<<number_of_shifts    


if __name__ == "__main__":
    p1 = [
        ([1, 2, 1, 3, 2, 5], [3, 5]),
        ([-1, 0], [-1, 0]),
        ([0, 1], [0, 1]),
        ([4, 4, 7, 9], [7, 9]),
        ([2, 1, 2, 3, 4, 1], [3, 4]),
        ([-5, -5, -3, 8], [-3, 8]),
        ([1 << 30, 7, 7, 3], [3, 1 << 30]),
    ]
    p2 = [
        (5, 7, 4), (0, 0, 0), (1, 2147483647, 0), (12, 15, 12),
        (6, 6, 6), (8, 9, 8), (2147483646, 2147483647, 2147483646), (3, 4, 0),
    ]
    passed = 0
    for i, (nums, e) in enumerate(p1, 1):
        r = single_number_iii(nums[:])
        ok = r is not None and sorted(r) == e
        passed += ok
        print(f"P1 test {i}: {'PASS' if ok else 'FAIL'} | {nums} -> {r} (expected {e} in any order)")
    for i, (l, rr, e) in enumerate(p2, 1):
        r = range_bitwise_and(l, rr)
        ok = r == e
        passed += ok
        print(f"P2 test {i}: {'PASS' if ok else 'FAIL'} | [{l}, {rr}] -> {r} (expected {e})")
    print(f"\n{passed}/{len(p1) + len(p2)} tests passed")

    random.seed(9)
    bad1 = bad2 = 0
    for _ in range(2000):
        a, b = random.sample(range(-1000, 1000), 2)
        pairs = random.sample([x for x in range(-1000, 1000) if x not in (a, b)], random.randint(0, 6))
        nums = pairs * 2 + [a, b]
        random.shuffle(nums)
        r = single_number_iii(nums[:])
        if r is None or sorted(r) != sorted([a, b]):
            bad1 += 1
        l = random.randint(0, 5000)
        rr = l + random.randint(0, 300)
        if range_bitwise_and(l, rr) != reduce(lambda x, y: x & y, range(l, rr + 1)):
            bad2 += 1
    print(f"Random check P1: {2000 - bad1}/2000 | P2: {2000 - bad2}/2000 match brute force")
