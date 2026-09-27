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
    best_len=float('inf')
    need_dict=Counter(t)
    need_count=len(need_dict)
    have={}
    have_count=0
    best_l=0
    best_r=0
    ## tackle edge case
    if len(s)<len(t) or len(t)==0:
        return ""
    
    for idx,val in enumerate(s):
        c=val
       
        if c in need_dict:
            have[c]=have.get(c,0)+1

            if need_dict[c]==have[c]:
                have_count+=1

        while have_count>=need_count:
            left_char=s[l]

            if r-l+1<best_len:
                best_len=r-l+1
                best_l=l
                best_r=r

            if left_char in need_dict:

                if need_dict[left_char]==have[left_char]:
                    have_count-=1

                have[left_char]-=1

            l+=1

            
        r+=1
    return s[best_l:best_r+1] if best_len<float('inf') else ""

    

    


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