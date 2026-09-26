"""
LeetCode 371: Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two integers
WITHOUT using the operators + and -.

Example:
    a = 1, b = 2
    Output: 3

    a = 2, b = 3
    Output: 5

Note: Python doesn't have fixed-width integers like Java/C++, so
this problem needs a bit of extra masking to behave correctly for
negative numbers -- the test cases below include negatives
specifically to make sure that's handled.
"""


def get_sum(a: int, b: int) -> int:
    # TODO: implement your solution here

    mask = 0xffffffff

    # Iterate till there is no carry 
    while (b & mask) != 0:
        
        
        carry_value = (a & b) << 1

      
        a = a ^ b
      
        
        b = carry_value 
    
    return a & mask if b > 0 else a
    


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        (1, 2, 3),               # classic case
        (2, 3, 5),                 # classic case
        (0, 0, 0),                   # both zero
        (5, 0, 5),                    # adding zero
        (-1, 1, 0),                     # negative + positive, cancels out
        (-2, -3, -5),                     # both negative
        (100, 200, 300),                    # larger numbers
        (-5, 5, 0),                           # symmetric cancellation
    ]

    passed = 0
    for i, (a, b, expected) in enumerate(tests, 1):
        result = get_sum(a, b)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  a={a}, b={b} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()