"""
BITWISE PRACTICE — Level 2 (P4–P7). Doc sections 5–6.
XOR facts: x ^ x = 0, x ^ 0 = x, order doesn't matter.
"""
from typing import List


def single_number(nums: List[int]) -> int:
    """P4. LeetCode 136. Every number appears twice except one. Find it.
    O(n) time, O(1) space."""
    number=0
    for num in nums:
        number=number^num
    return number

def hamming_distance(x: int, y: int) -> int:
    """P5. LeetCode 461. In how many bit positions do x and y differ?
    Hint: which operator gives 1 exactly where two bits differ?"""
    z=x^y
    i=0
    res=0
    while i<32:
        if z%2==1:
            res+=1
        z=z>>1    
        i+=1
        

    return res


def is_power_of_four(n: int) -> bool:
    """P6. LeetCode 342. A power of two whose single 1 sits at an EVEN position (0, 2, 4...).
    1 = 1, 4 = 100, 16 = 10000 are powers of four; 2 = 10 and 8 = 1000 are not.
    Hint: 0x55555555 = 0101...0101 has 1s only at even positions."""
    # TODO
    return n > 0 and n & (n - 1) == 0 and (n & 0x55555555) != 0


def find_complement(num: int) -> int:
    """P7. LeetCode 476. Flip every bit of num's binary form (no leading zeros).
    5 (101) -> 2 (010).   Hint: build a mask of all 1s exactly as wide as num
    (num.bit_length() tells you how wide), then flip with XOR."""
    # TODO
    
    mask=0
    for i in range(0,num.bit_length()):
        mask = mask|1<<i
    return mask^num  


def run_tests():
    total = passed = 0
    def check(label, got, exp):
        nonlocal total, passed
        total += 1; ok = got == exp; passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {label:<34} got {got!r}, expected {exp!r}")

    for nums, e in [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1), ([-1, 5, 5], -1), ([7, 3, 3, 9, 9], 7), ([0, 8, 8], 0)]:
        check(f"P4 single_number({nums})", single_number(list(nums)), e)
    for x, y, e in [(1, 4, 2), (3, 1, 1), (0, 0, 0), (255, 0, 8), (7, 7, 0), (8, 7, 4)]:
        check(f"P5 hamming_distance({x}, {y})", hamming_distance(x, y), e)
    for n, e in [(1, True), (4, True), (16, True), (64, True), (256, True), (2, False), (8, False), (5, False), (0, False), (-4, False)]:
        check(f"P6 is_power_of_four({n})", is_power_of_four(n), e)
    for n, e in [(5, 2), (1, 0), (10, 5), (7, 0), (8, 7), (2, 1)]:
        check(f"P7 find_complement({n})", find_complement(n), e)
    print(f"\n{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
