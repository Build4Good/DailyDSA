"""
REVISION — LeetCode 5: Longest Palindromic Substring
Return the longest palindromic substring of s.
(Where several answers tie, any one is accepted — tests check length + validity.)
"""


def longest_palindrome(s: str) -> str:
    # TODO: from memory
    max_len=0
    
    best_l=0
    best_r=0
    for i in range(len(s)):

        ##lets check for odd length palidnrome 
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 >max_len:
                max_len=r-l+1
                best_l=l
                best_r=r
            l-=1
            r+=1 

        ## for even length pal they will start +1
        l,r=i,i+1   
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 >max_len:
                max_len=r-l+1
                best_l=l
                best_r=r
            l-=1
            r+=1 


    return s[best_l:best_r+1]        


def run_tests():
    tests = [
        ("babad", 3), ("cbbd", 2), ("a", 1), ("", 0), ("ac", 1),
        ("racecar", 7), ("aaaa", 4), ("abacdfgdcaba", 3),
    ]
    passed = 0
    for i, (s, exp_len) in enumerate(tests, 1):
        res = longest_palindrome(s)
        ok = res is not None and len(res) == exp_len and res in s and res == res[::-1]
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  s={s!r} -> got {res!r}, expected length {exp_len}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()