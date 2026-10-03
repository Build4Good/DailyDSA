"""REVISION — LeetCode 11: Container With Most Water. Max area between two lines."""
from typing import List


def max_area(height: List[int]) -> int:
    # TODO: from memory
    pass


def run_tests():
    tests = [([1,8,6,2,5,4,8,3,7], 49), ([1,1], 1), ([4,3,2,1,4], 16), ([1,2,1], 2),
             ([1,2,4,3], 4), ([2,3,4,5,18,17,6], 17), ([5,5,5,5], 15)]
    passed = 0
    for i, (h, exp) in enumerate(tests, 1):
        res = max_area(list(h)); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  {h} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
