"""
LeetCode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An anagram is a word formed by rearranging the letters of another,
using all the original letters exactly once.

Example:
    s = "anagram", t = "nagaram"
    Output: True
"""
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    counter_s=Counter(s)
    counter_t=Counter(t)
    return counter_s==counter_t
    pass


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("anagram", "nagaram", True),     # classic case
        ("rat", "car", False),             # same length, different letters
        ("a", "a", True),                   # single character match
        ("", "", True),                      # both empty
        ("a", "ab", False),                  # different lengths
        ("aacc", "ccac", False),             # same letters present, but WRONG counts
        ("aabbcc", "abcabc", True),          # counts match, order fully scrambled
    ]

    passed = 0
    for i, (s, t, expected) in enumerate(tests, 1):
        result = is_anagram(s, t)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r}, t={t!r} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()