"""
LeetCode 338: Counting Bits
Return an array ans of length n+1 where ans[i] = number of 1s in binary(i).
Aim for O(n): reuse earlier answers instead of counting each number from scratch.
Hint: ans[i] relates to ans[i >> 1] (i without its last bit) plus (i & 1).
"""
from typing import List


def count_bits(n: int) -> List[int]:
    # TODO
    ans=[0]*(n+1)
    current_offset=1  #2 power 0 in begining 
    for i in range(1,n+1):
        if current_offset*2 == i:
            current_offset=i

        ans[i]=1+ans[i-current_offset]    
    return ans
    


def run_tests():
    tests = [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2]), (0, [0]), (1, [0, 1]),
             (8, [0, 1, 1, 2, 1, 2, 2, 3, 1])]
    passed = 0
    for i, (n, exp) in enumerate(tests, 1):
        res = count_bits(n); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  n={n} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()