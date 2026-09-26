"""
REVISION — LeetCode 76: Minimum Window Substring
Return the smallest substring of s containing every character of t
(including duplicates). Return "" if none exists.
"""
from collections import Counter

def min_window(s: str, t: str) -> str:
    # TODO: from memory
    l=0
    r=0
    
    best_len=len(s)+1
    best_l=0
    need_dict=Counter(t)
    need_count=len(need_dict)
    have_dict={}
    str_found=False
    have_count=0

    ## tackle edge case
    if len(s)<len(t) or len(t)==0:
        return ""

    while r<len(s):
        c=s[r]
        
        if c in need_dict:
            have_dict[c]=have_dict.get(c,0)+1
            if have_dict[c]==need_dict[c]:
                have_count+=1 
        while have_count>=need_count:
            str_found=True
            if r-l+1 <best_len:
                best_len=r-l+1
                best_l=l
            left_char=s[l]
            l+=1

            if left_char in need_dict:
                if need_dict[left_char]==have_dict[left_char]:
                    have_dict[left_char]=have_dict.get(left_char,0)-1
                    have_count-=1
                else:
                    have_dict[left_char]=have_dict.get(left_char,0)-1    
        r+=1            

    return s[best_l:best_l+best_len] if best_len<(len(s)+1) else ""

    


def run_tests():
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("", "a", ""),
        ("a", "", ""),
        ("ab", "b", "b"),
        ("aa", "aa", "aa"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
    ]
    passed = 0
    for i, (s, t, exp) in enumerate(tests, 1):
        res = min_window(s, t)
        ok = res == exp
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  s={s!r}, t={t!r} -> got {res!r}, expected {exp!r}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()