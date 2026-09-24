"""
LeetCode 647: Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example:
    s = "abc"
    Output: 3  ("a", "b", "c")

    s = "aaa"
    Output: 6  ("a", "a", "a", "aa", "aa", "aaa")
"""


def count_substrings(s: str) -> int:
    count=0

    for i in range(len(s)):
        ### odd length palindrome 
        l,r=i,i
        while l>=0 and r <len(s) and (s[l]==s[r]):
            count+=1
            l-=1
            r+=1

        ### for even length 
        l,r=i,i+1
        while l>=0 and r <len(s) and (s[l]==s[r]):
            count+=1
            l-=1
            r+=1

    return count


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("abc", 3),                 # no repeats, no multi-char palindromes
        ("aaa", 6),                   # all same character
        ("a", 1),                      # single character
        ("", 0),                        # empty string
        ("aa", 3),                       # "a","a","aa"
        ("racecar", 10),                  # a real palindrome with nested ones inside
        ("abba", 6),                        # even-length palindrome nested inside
        ("abacdfgdcaba", 14),                 # mix of many small palindromes, no huge one
    ]

    passed = 0
    for i, (s, expected) in enumerate(tests, 1):
        result = count_substrings(s)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()