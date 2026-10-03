"""REVISION — LeetCode 191: Number of 1 Bits. Use the n & (n - 1) trick this time."""


def hamming_weight(n: int) -> int:
    # TODO: from memory
    pass


def run_tests():
    tests = [(11,3),(128,1),(2147483645,30),(1,1),(0,0),(255,8),(1024,1),(7,3)]
    passed = 0
    for i, (n, exp) in enumerate(tests, 1):
        res = hamming_weight(n); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  n={n} ({bin(n)}) -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
