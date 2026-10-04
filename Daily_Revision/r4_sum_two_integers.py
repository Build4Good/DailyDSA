"""REVISION — LeetCode 371: Sum of Two Integers without + or -. Handle negatives (Python masking)."""


def get_sum(a: int, b: int) -> int:
    # TODO: from memory
    ## keep a as sum without carry and b as carry
    mask=0xffffffff
    while (mask&b)>0:
        a,b=a^b,((a&b)<<1)

    return (mask&a) if b>0 else a
def run_tests():
    tests = [(1,2,3),(2,3,5),(0,0,0),(5,0,5),(-1,1,0),(-2,-3,-5),(100,200,300),(-5,5,0),
             (-1,-1,-2),(3,-2,1),(-1000,1000,0),(-1000,-1000,-2000)]
    passed = 0
    for i, (a, b, exp) in enumerate(tests, 1):
        res = get_sum(a, b); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  {a} + {b} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
