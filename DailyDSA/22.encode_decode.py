"""
LeetCode 271: Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/
(Premium on LeetCode, but a very common interview question -- freely
solvable and testable here.)

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of
strings.

Your encode() and decode() functions must be able to handle ANY
possible characters within the strings, including empty strings,
strings that contain your chosen delimiter, digits, etc.

Example:
    strs = ["hello", "world"]
    encoded = encode(strs)          # some single string
    decode(encoded) == strs         # must round-trip exactly
"""

from typing import List


def encode(strs: List[str]) -> str:
    # TODO: implement your solution here
    res=""
    for s in strs:
        res+=str(len(s))+"#"+s

    
    return res


def decode(s: str) -> List[str]:
    # TODO: implement your solution here
    res, i =[],0

    while i < len(s):
        j=i
        while s[j] !="#":
            j+=1
        len_str=int(s[i:j])
        res.append(s[j+1:j+1+len_str])
        i=j+1+len_str
    return res        


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ["hello", "world"],                      # classic case
        [],                                        # empty list
        [""],                                        # a list containing one empty string
        ["", "", ""],                                  # multiple empty strings
        ["a,b", "c,d"],                                  # strings that contain a comma
        ["4#3", "hello#world"],                            # strings that contain '#' -- a common naive delimiter choice
        ["single"],                                          # a single, one-element list
        ["with space", "another one", ""],                     # spaces mixed with an empty string
    ]

    passed = 0
    for i, strs in enumerate(tests, 1):
        encoded = encode(strs)
        decoded = decode(encoded)
        ok = decoded == strs
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  strs={strs!r} -> encoded={encoded!r} -> decoded={decoded!r}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()