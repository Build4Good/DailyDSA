"""
REVISION from memory: Longest Repeating Character Replacement (LeetCode 424)

Given a string s of uppercase letters and an int k, you may change at most k characters.
Return the length of the longest substring that can be made of one repeated letter.
Target: O(n) sliding window. No notes, no hints - 20-25 minutes.
"""

import random
from typing import List


def character_replacement(s: str, k: int) -> int:
    # TODO
    freq_count={}
    l=0
    r=0
    res=0
    while r<len(s):
        freq_count[s[r]]=freq_count.get(s[r],0)+1
        max_count = max(freq_count.values())

        while (r-l+1)-max_count>k:
            freq_count[s[l]]=freq_count.get(s[l])-1
            l+=1
        res=max(res,r-l+1)

        r+=1
    return res

def _brute(s, k):
    best = 0
    for i in range(len(s)):
        cnt = {}
        for j in range(i, len(s)):
            cnt[s[j]] = cnt.get(s[j], 0) + 1
            if (j - i + 1) - max(cnt.values()) <= k:
                best = max(best, j - i + 1)
    return best


if __name__ == "__main__":
    tests = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("", 0, 0),
        ("A", 0, 1),
        ("AAAA", 0, 4),
        ("ABCD", 0, 1),
        ("ABCD", 4, 4),
        ("ABBB", 0, 3),
        ("AAABBBCCC", 2, 5),
        ("ABAA", 0, 2),
        ("BAAAB", 2, 5),
    ]
    passed = 0
    for i, (s, k, e) in enumerate(tests, 1):
        r = character_replacement(s, k)
        ok = r == e
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | s={s!r}, k={k} -> {r} (expected {e})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(11)
    bad = 0
    for _ in range(3000):
        s = "".join(random.choice("ABC") for _ in range(random.randint(0, 12)))
        k = random.randint(0, 4)
        if character_replacement(s, k) != _brute(s, k):
            bad += 1
            if bad == 1:
                print("First random mismatch:", repr(s), k, "expected", _brute(s, k))
    print(f"Random check: {3000 - bad}/3000 match brute force")
