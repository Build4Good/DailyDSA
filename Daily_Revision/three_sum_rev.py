"""
REVISION — LeetCode 15: 3Sum
Return all UNIQUE triplets [a, b, c] with a + b + c == 0.
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # TODO: from memory
    list_pairs=[]
    nums.sort()
    target=0
    for i in range(len(nums)):
        l=i+1
        r=len(nums)-1

        if i>0 and nums[i]==nums[i-1]:
            continue

        while l<r:
            total=nums[l]+nums[r]+nums[i]

            if total>target:
                ###value bigger reduce larger number that is decrement r
                r-=1
            elif total<target:
                ###value smaller increment smaller number increase l
                l+=1
            else:
                list_pairs.append([nums[i],nums[l],nums[r]])

                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1

                r-=1

                while nums[r]==nums[r+1] and l<r:
                    r-=1

    
    # lets first sort the input 
    return list_pairs


def normalize(result):
    return sorted(sorted(t) for t in result)


def run_tests():
    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([1, 2, -2, -1], []),
        ([], []),
        ([1, -1], []),
    ]
    passed = 0
    for i, (nums, exp) in enumerate(tests, 1):
        res = three_sum(list(nums))
        ok = normalize(res or []) == normalize(exp)
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  nums={nums} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()