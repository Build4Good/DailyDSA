"""
BITWISE PRACTICE — Level 3 (P8–P10). Doc section 7.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """P8. LeetCode 78. Return every subset, using BITMASKS (no recursion).
    For n items, loop mask from 0 to 2^n - 1 (that's 1 << n masks).
    Bit i of the mask ON  ->  nums[i] is in this subset.
    [a, b, c]:  mask 101 -> [a, c]"""
    # TODO
    pass


def single_number_iii(nums: List[int]) -> List[int]:
    """P9. LeetCode 260. Exactly TWO numbers appear once; every other number appears twice.
    Return the two (any order). O(n) time, O(1) space.
    Hint 1: XOR everything -> you get a ^ b (the pairs cancel).
    Hint 2: any 1 bit in a ^ b is a position where a and b DIFFER. Grab one with x & -x.
    Hint 3: split nums into two groups by that bit; XOR each group separately."""
    # TODO
    pass


def range_bitwise_and(left: int, right: int) -> int:
    """P10. LeetCode 201. AND of every number from left to right, inclusive.
    Must NOT loop over the range (it can be ~2 billion numbers).
    Hint: the answer is the common binary PREFIX of left and right, padded with zeros.
    Shift both right until they're equal, counting the shifts; then shift back."""
    # TODO
    pass


def run_tests():
    total = passed = 0
    def check(label, got, exp):
        nonlocal total, passed
        total += 1; ok = got == exp; passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {label:<40} got {got!r}, expected {exp!r}")
    norm = lambda x: sorted(sorted(s) for s in x) if x is not None else None

    check("P8 subsets([1,2,3])", norm(subsets([1, 2, 3])), norm([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))
    check("P8 subsets([0])", norm(subsets([0])), norm([[], [0]]))
    check("P8 subsets([]) -> just the empty set", norm(subsets([])), [[]])
    r = subsets([1, 2, 3, 4])
    check("P8 subsets of 4 items -> 16 subsets", len(r) if r is not None else None, 16)

    for nums, e in [([1, 2, 1, 3, 2, 5], [3, 5]), ([-1, 0], [-1, 0]), ([0, 1], [0, 1]),
                    ([4, 7, 4, 9, 7, 2], [2, 9]), ([10, 3], [3, 10]), ([-5, 6, 6, -3], [-5, -3])]:
        res = single_number_iii(list(nums))
        check(f"P9 single_number_iii({nums})", sorted(res) if res else res, sorted(e))

    for l, r_, e in [(5, 7, 4), (0, 0, 0), (1, 2147483647, 0), (12, 15, 12), (6, 6, 6), (26, 30, 24), (1, 1, 1)]:
        check(f"P10 range_bitwise_and({l}, {r_})", range_bitwise_and(l, r_), e)

    print(f"\n{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
