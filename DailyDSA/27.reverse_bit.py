"""
LeetCode 190: Reverse Bits
Reverse the bits of a 32-bit unsigned integer.
Idea: 32 times -- take n's last bit (n & 1), push it onto the result
(res << 1 | bit), then shift n right. Loop exactly 32 times, not 'while n',
or leading zeros won't move to the end.
"""


def reverse_bits(n: int) -> int:
    # TODO
    res=0

    ## shift number towards right for current i and a to get the bit , now we need to 
    for i in range(32):
        current_bit = (n>>i)&1
        res = res | (current_bit<<(31-i))
    return res

def run_tests():
    tests = [(43261596, 964176192),      # 00000010100101000001111010011100
             (4294967293, 3221225471),   # 11111111111111111111111111111101
             (0, 0), (1, 2147483648), (2147483648, 1)]
    passed = 0
    for i, (n, exp) in enumerate(tests, 1):
        res = reverse_bits(n); ok = res == exp; passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  n={n} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()