"""
NEW: Set Matrix Zeroes (LeetCode 73)

Given an m x n integer matrix, if an element is 0, set its ENTIRE row and column to 0.
Do it IN PLACE (modify `matrix`, return nothing).
Step 1: get it working with O(m + n) extra space.
Step 2 (stretch): O(1) extra space.
"""

import copy
import random
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    # TODO
    
    ### first check if any row or column is zero
    rows_to_set_zero=set()
    columns_to_set_zero=set()

    for row in range(len(matrix)):

        for col in range(len(matrix[row])):

            if matrix[row][col]==0:
                rows_to_set_zero.add(row)
                columns_to_set_zero.add(col)
                
    for row in range(len(matrix)):
    
        for col in range(len(matrix[row])):
    
            if row in rows_to_set_zero or col in columns_to_set_zero:
                matrix[row][col]=0


                    
                    
    


def _brute(matrix):
    m = copy.deepcopy(matrix)
    rows = {i for i, row in enumerate(m) for v in row if v == 0}
    cols = {j for row in m for j, v in enumerate(row) if v == 0}
    for i in range(len(m)):
        for j in range(len(m[0]) if m else 0):
            if i in rows or j in cols:
                m[i][j] = 0
    return m


if __name__ == "__main__":
    tests = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[1]],
        [[0]],
        [[1, 2, 3]],
        [[1], [0], [3]],
        [[1, 0], [1, 1]],
        [[0, 0], [0, 0]],
        [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]],
        [[-1, 2], [3, 4]],
    ]
    passed = 0
    for i, m in enumerate(tests, 1):
        exp = _brute(m)
        got = copy.deepcopy(m)
        ret = set_zeroes(got)
        ok = got == exp and ret is None
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {m} -> {got} (expected {exp})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(13)
    bad = 0
    for _ in range(3000):
        r, c = random.randint(1, 6), random.randint(1, 6)
        m = [[random.choice([0, 1, 2, 3, 4, 5, 6]) for _ in range(c)] for _ in range(r)]
        got = copy.deepcopy(m)
        set_zeroes(got)
        if got != _brute(m):
            bad += 1
            if bad == 1:
                print("First random mismatch:", m, "expected", _brute(m), "got", got)
    print(f"Random check: {3000 - bad}/3000 match brute force")
