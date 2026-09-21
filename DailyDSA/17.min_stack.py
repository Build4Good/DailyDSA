"""
LeetCode 155: Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time O(1).

Implement the MinStack class:
    MinStack() initializes the stack object.
    push(val)  pushes val onto the stack.
    pop()      removes the element on top of the stack.
    top()      gets the top element.
    getMin()   retrieves the minimum element in the stack.

Example:
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.getMin()  -> -3
    stack.pop()
    stack.top()     -> 0
    stack.getMin()  -> -2   (after popping -3, min goes back to -2)
"""

from collections import deque

class MinStack:
    def __init__(self):
        # TODO: implement your solution here
        self.stk=[]
        self.min_stk=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk and val <= self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])    

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    passed = 0
    total = 0

    def check(actual, expected, label):
        nonlocal passed, total
        total += 1
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"{status}  {label} -> got {actual}, expected {expected}")

    # Test 1: classic example from the problem
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    check(s.getMin(), -3, "getMin after pushing -2,0,-3")
    s.pop()
    check(s.top(), 0, "top after popping -3")
    check(s.getMin(), -2, "getMin after popping -3 (min reverts to -2)")

    # Test 2: min changes correctly across multiple pops
    s2 = MinStack()
    s2.push(5)
    s2.push(3)
    s2.push(7)
    s2.push(1)
    check(s2.getMin(), 1, "getMin with [5,3,7,1]")
    s2.pop()  # remove 1
    check(s2.getMin(), 3, "getMin after popping 1 -> min is 3")
    s2.pop()  # remove 7
    check(s2.getMin(), 3, "getMin after popping 7 -> min still 3")
    s2.pop()  # remove 3
    check(s2.getMin(), 5, "getMin after popping 3 -> min reverts to 5")

    # Test 3: duplicate minimums
    s3 = MinStack()
    s3.push(2)
    s3.push(2)
    s3.push(1)
    check(s3.getMin(), 1, "getMin with duplicate 2's and a 1")
    s3.pop()  # remove 1
    check(s3.getMin(), 2, "getMin after popping 1 -> min is 2 (still two 2's)")

    print()
    print(f"{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()