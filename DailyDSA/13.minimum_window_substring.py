"""
LeetCode 76: MinimumWindowSubstring


Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included
in the window. If no such substring exists, return the empty string "".

Example:
    s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

    s = "a", t = "aa"
    Output: ""  (t needs TWO a's, s only has one)
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    l=0
    r=0
    need=Counter(t)
    need_count=len(need)
    have={}
    have_count=0
    res=s     
    res_found=False
    if len(s)<len(t) or len(t)==0:
        return ""
    else:
        while r<len(s):
            c=s[r]
            if c in need:
                have[s[r]]=have.get(s[r],0)+1
                if have[c]==need[c]:
                    have_count+=1
            while have_count>=need_count:
                res_found=True
                res= s[l:r+1]   if len(s[l:r+1])<len(res) else res
                left_char=s[l]
                l+=1
                
                if left_char in need:

                    if have[left_char]==need[left_char]:
                        have[left_char]= have.get(left_char,0)-1
                        have_count-=1
                    else:
                        have[left_char]= have.get(left_char,0)-1 
            r+=1

    return res if res_found  else ""        







# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),   # classic case
        ("a", "a", "a"),                      # smallest possible match
        ("a", "aa", ""),                       # t needs a DUPLICATE s doesn't have
        ("", "a", ""),                          # empty s
        ("a", "", ""),                           # empty t (no requirement -- LeetCode guarantees t non-empty, but worth handling)
        ("ab", "b", "b"),                        # match is a single character, not the whole string
        ("aa", "aa", "aa"),                      # duplicates needed, exactly available
        ("cabwefgewcwaefgcf", "cae", "cwae"),    # window isn't obvious, needs real tracking
    ]

    passed = 0
    for i, (s, t, expected) in enumerate(tests, 1):
        result = min_window(s, t)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r}, t={t!r} -> got {result!r}, expected {expected!r}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()