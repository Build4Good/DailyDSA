"""REVISION — LeetCode 155: Min Stack. push, pop, top, getMin — all O(1)."""


class MinStack:
    def __init__(self):
        # TODO: from memory
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val<self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])   



    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def run_tests():
    passed = total = 0
    def check(a, e, label):
        nonlocal passed, total
        total += 1; ok = a == e; passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {label} -> got {a}, expected {e}")
    s = MinStack(); s.push(-2); s.push(0); s.push(-3)
    check(s.getMin(), -3, "getMin [-2,0,-3]"); s.pop()
    check(s.top(), 0, "top after pop"); check(s.getMin(), -2, "getMin reverts")
    s2 = MinStack()
    for v in (5, 3, 7, 1): s2.push(v)
    check(s2.getMin(), 1, "getMin [5,3,7,1]"); s2.pop(); check(s2.getMin(), 3, "after pop 1")
    s2.pop(); check(s2.getMin(), 3, "after pop 7"); s2.pop(); check(s2.getMin(), 5, "after pop 3")
    s3 = MinStack(); s3.push(2); s3.push(2); s3.push(1)
    check(s3.getMin(), 1, "dup 2s + 1"); s3.pop(); check(s3.getMin(), 2, "after pop 1 (still two 2s)")
    s4 = MinStack()
    for v in (5, 7, 7, 3): s4.push(v)
    s4.pop(); s4.pop(); check(s4.getMin(), 5, "stress: [5,7,7,3] pop 3 and a 7")
    print(f"\n{passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
