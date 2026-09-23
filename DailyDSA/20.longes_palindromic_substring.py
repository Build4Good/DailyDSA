"""
LeetCode 5: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example:
    s = "babad"
    Output: "bab"  (note: "aba" is also a valid answer)

    s = "cbbd"
    Output: "bb"
"""


def longest_palindrome(s: str) -> str:
    res=""
    resLen=0

    for i in range(len(s)):
        ### for odd lenght palindrome l&r to start from same place
        l,r=i,i

        while l>=0 and r <len(s) and (s[l]==s[r]):
            if r-l+1 > resLen:
                res=s[l:r+1]
                resLen=r-l+1
            r+=1
            l-=1

        ### for even length palindrom l =i r=i+1
        l,r=i,i+1
        while l>=0 and r <len(s) and (s[l]==s[r]):
            if r-l+1 > resLen:
                res=s[l:r+1]
                resLen=r-l+1
            r+=1
            l-=1
               
    return res


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# (for cases with multiple valid answers, we check length + palindrome validity)
# ─────────────────────────────────────────────

def is_valid_palindrome_substring(s, sub):
    if sub not in s:
        return False
    return sub == sub[::-1]


def run_tests():
    tests = [
        ("babad", 3),           # multiple valid answers ("bab" or "aba"), check length 3
        ("cbbd", 2),              # "bb" -- even-length palindrome
        ("a", 1),                  # single character
        ("", 0),                    # empty string
        ("ac", 1),                   # no real palindrome longer than 1 char
        ("racecar", 7),                # the whole string is a palindrome
        ("aaaa", 4),                     # all same character
        ("abacdfgdcaba", 3),               # longest is "aba" (appears twice), not the whole string
    ]

    passed = 0
    for i, (s, expected_len) in enumerate(tests, 1):
        result = longest_palindrome(s)
        ok = len(result) == expected_len and is_valid_palindrome_substring(s, result)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r} -> got {result!r} (len={len(result)}), expected length {expected_len}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()