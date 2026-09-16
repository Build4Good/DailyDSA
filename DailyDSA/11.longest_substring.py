"""
LeetCode 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without
repeating characters.

Example:
    s = "abcabcbb"
    Output: 3  (the answer is "abc", with a length of 3)
"""


def length_of_longest_substring(s: str) -> int:
    l=0 
    r=0
    window=set()
    max_len=0
    while r<len(s):

        while s[r] in window:
            window.remove(s[l])
            l+=1
        window.add(s[r])
        max_len = max(max_len, r - l+1)
        r+=1
    



    return max_len


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("abcabcbb", 3),        # classic case -- "abc"
        ("bbbbb", 1),            # all repeated -- single character window
        ("pwwkew", 3),           # "wke" -- best window isn't at the start
        ("", 0),                 # empty string
        (" ", 1),                # single space, still a valid character
        ("au", 2),               # two distinct characters
        ("dvdf", 3),             # repeats with a non-adjacent duplicate -- "vdf"
        ("abba", 2),             # a duplicate reappearing after the window already moved past it once
    ]

    passed = 0
    for i, (s, expected) in enumerate(tests, 1):
        result = length_of_longest_substring(s)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()