"""
DSA REVISION - Week 1 (Day 8). From memory: no notes, no peeking at old code.
Your two weakest problems from the bitwise set.

R1. LeetCode 342: Power of Four
    https://leetcode.com/problems/power-of-four/
    Return True if n is a power of four (1, 4, 16, 64, ...). Try for O(1), no loop.

R2. LeetCode 260: Single Number III
    https://leetcode.com/problems/single-number-iii/
    Exactly two numbers appear once, every other number appears twice.
    Return the two (any order). O(n) time, O(1) space.

R3. LeetCode 56: Merge Intervals
    https://leetcode.com/problems/merge-intervals/
    Merge all overlapping intervals (touching ends DO merge). Don't change the input.

R4. LeetCode 78: Subsets  - use BITMASKS, no recursion
    https://leetcode.com/problems/subsets/
    Return every subset of nums (any order).

Rule: write all four, run, THEN send. If stuck for > 10 min on one, write down
exactly where you are stuck - that's the useful part of revision.
"""

from typing import List


def is_power_of_four(n: int) -> bool:
    # TODO
    return n>0 and (n & (n-1))==0 and ((n & 0x55555555)!=0)


def single_number_iii(nums: List[int]) -> List[int]:
    # TODO
    ### we will xor all , which will give us a^b two number which dont cancel out , x&-x when we do that it will give us only last signifcant bit and when we do a xor where its equal to 1 we get a , where its 0 we get another number
    mask=0
    for num in nums:
        mask^=num
    ## mask now is a^b two number lets add with -mask to get last signifciant bit 
    bit_l=mask&(-mask)

    ## now lets and all again to get the detials one xor op will give 1 other will give 0 where they differ on xor op a^b
    a,b=0,0
    for num in nums:

        if bit_l&num==0:
            a^=num
        else:
            b^=num

    return [a,b]            







def merge(intervals: List[List[int]]) -> List[List[int]]:
    # TODO
    interval_up= [ intv[:]     for intv in sorted(intervals)  ]
    result=[]
    result.append([interval_up[0][0],interval_up[0][1]])
    
    for i in range (1,len(interval_up)):

        if interval_up[i][0]<=result[-1][1]:
            result[-1][-1]=max(result[-1][1],interval_up[i][1])
            
        else:
            result.append([interval_up[i][0],interval_up[i][1]])    

    return result


def subsets(nums: List[int]) -> List[List[int]]:
    # TODO
    result=[]

    for num in range(1<<len(nums)):
        lst=[]
        for i in range(0,len(nums)):
            if num & (1<<i) !=0 :
                lst.append(nums[i])
        
        result.append(lst)       

    return result



# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────

if __name__ == "__main__":
    total = passed = 0

    def check(label, got, exp):
        global total, passed
        total += 1
        ok = got == exp
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {label:<38} got {got!r}, expected {exp!r}")

    for n, e in [(1, True), (4, True), (16, True), (64, True), (1 << 30, True),
                 (0, False), (-4, False), (2, False), (8, False), (32, False),
                 (5, False), (12, False), (2**31 - 1, False)]:
        check(f"R1 is_power_of_four({n})", is_power_of_four(n), e)

    for nums, e in [([1, 2, 1, 3, 2, 5], [3, 5]), ([-1, 0], [-1, 0]), ([0, 1], [0, 1]),
                    ([4, 4, 7, 9], [7, 9]), ([-5, -3, 2, 2], [-5, -3]),
                    ([2**31 - 1, -2**31, 6, 6], [-2**31, 2**31 - 1]),
                    ([10, 20, 10, 30, 20, 40, 50, 50], [30, 40])]:
        res = single_number_iii(list(nums))
        check(f"R2 single_number_iii({nums[:4]}...)", sorted(res) if res else res, sorted(e))

    for iv, e in [([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
                  ([[1, 4], [4, 5]], [[1, 5]]), ([[4, 7], [1, 4]], [[1, 7]]),
                  ([[1, 10], [2, 3], [4, 5]], [[1, 10]]), ([[1, 4]], [[1, 4]])]:
        original = [x[:] for x in iv]
        res = merge(iv)
        check(f"R3 merge({original})", sorted(res) if res else res, e)
        check(f"R3 input unchanged", iv, original)

    norm = lambda x: sorted(sorted(s) for s in x) if x is not None else None
    check("R4 subsets([1,2,3])", norm(subsets([1, 2, 3])),
          norm([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]))
    check("R4 subsets([0])", norm(subsets([0])), [[], [0]])
    check("R4 subsets([])", norm(subsets([])), [[]])
    r = subsets([1, 2, 3, 4, 5])
    check("R4 subsets of 5 items -> 32", len(r) if r is not None else None, 32)

    print(f"\n{passed}/{total} tests passed")
