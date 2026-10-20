"""
LADDER 2/4 (sliding window) - REVISION from memory: Longest Substring Without Repeating Characters (LeetCode 3)

Return the length of the longest substring of s with no repeated characters.
Target: O(n) sliding window. 15-20 minutes.
"""

import random


def length_of_longest_substring(s: str) -> int:
    # TODO
    seen=set()
    l,r=0,0
    max_l=0

    while r<len(s):

        if s[r] not in seen:
            seen.add(s[r])
            max_l=max(max_l,r-l+1)
        else:
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])    
        r+=1
    return max_l    

def _brute(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
        ("abcdef", 6),
        ("aab", 2),
    ]
    passed = 0
    for i, (s, e) in enumerate(tests, 1):
        r = length_of_longest_substring(s)
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | {s!r} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(5)
    bad = 0
    for _ in range(3000):
        s = "".join(random.choice("abcd ") for _ in range(random.randint(0, 14)))
        if length_of_longest_substring(s) != _brute(s):
            bad += 1
            if bad == 1:
                print("First random mismatch:", repr(s), "expected", _brute(s))
    print(f"Random check: {3000 - bad}/3000 match brute force")
