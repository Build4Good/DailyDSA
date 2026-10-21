"""
LADDER 4/4 (sliding window) - REVISION from memory: Minimum Window Substring (LeetCode 76)

Return the SHORTEST substring of s that contains every character of t (with multiplicity).
Return "" if none exists. If several have the same minimum length, any one is fine
(tests check the length and validity, not which one).
Target: O(len(s) + len(t)) sliding window. 25-30 minutes.
"""

import random
from collections import Counter


def min_window(s: str, t: str) -> str:
    # TODO
    pass


def _valid(sub, t):
    need = Counter(t)
    have = Counter(sub)
    return all(have[c] >= n for c, n in need.items())


def _brute_len(s, t):
    if not t:
        return 0
    best = None
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if _valid(s[i:j], t):
                if best is None or j - i < best:
                    best = j - i
                break
    return best if best is not None else 0


def _check(s, t, got):
    exp = _brute_len(s, t)
    if exp == 0:
        return got == ""
    return isinstance(got, str) and len(got) == exp and got in s and _valid(got, t)


if __name__ == "__main__":
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("", "a", ""),
        ("ab", "b", "b"),
        ("aa", "aa", "aa"),
        ("bba", "ab", "ba"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
        ("abc", "d", ""),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ]
    passed = 0
    for i, (s, t, e) in enumerate(tests, 1):
        r = min_window(s, t)
        ok = _check(s, t, r)
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'} | s={s!r}, t={t!r} -> {r!r} (expected e.g. {e!r})")
    print(f"\n{passed}/{len(tests)} tests passed")

    random.seed(9)
    bad = 0
    for _ in range(3000):
        s = "".join(random.choice("abc") for _ in range(random.randint(0, 12)))
        t = "".join(random.choice("abc") for _ in range(random.randint(1, 4)))
        got = min_window(s, t)
        if not _check(s, t, got):
            bad += 1
            if bad == 1:
                print("First random mismatch:", repr(s), repr(t), "got", repr(got), "expected length", _brute_len(s, t))
    print(f"Random check: {3000 - bad}/3000 match brute force")
