"""
LeetCode 125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
    s = "A man, a plan, a canal: Panama"
    Output: True  (becomes "amanaplanacanalpanama")

    s = "race a car"
    Output: False  (becomes "raceacar")
"""


def is_palindrome(s: str) -> bool:
    # TODO: implement your solution here
    l=0
    r=len(s)-1

    while l<r:
        
        if not s[l].isalnum():
            l+=1
            continue
        if not s[r].isalnum():
            r-=1
            continue

        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
    
    return True



    


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("A man, a plan, a canal: Panama", True),   # classic case, punctuation + case
        ("race a car", False),                        # not a palindrome
        (" ", True),                                    # single space -- after cleaning, empty string, vacuously true
        ("0P", False),                                   # short, mixed alnum, not a palindrome
        ("Was it a car or a cat I saw?", True),          # longer, punctuation-heavy
        ("ab_a", True),                                   # underscore is NOT alphanumeric -- must be ignored
        ("12321", True),                                   # numeric palindrome
        ("12345", False),                                    # numeric, not a palindrome
    ]

    passed = 0
    for i, (s, expected) in enumerate(tests, 1):
        result = is_palindrome(s)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()