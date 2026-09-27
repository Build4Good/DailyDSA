"""
REVISION — LeetCode 647: Palindromic Substrings
Return how many palindromic substrings s contains.
"""


def count_substrings(s: str) -> int:
    # TODO: from memory
    count=0

    for i in range(len(s)):

        ## for odd lenght palindromes 
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
        ##for even lenght

        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            count+=1
            l-=1
            r+=1    
    return count

def run_tests():
    tests = [("abc", 3), ("aaa", 6), ("a", 1), ("", 0), ("aa", 3),
             ("racecar", 10), ("abba", 6), ("abacdfgdcaba", 14)]
    passed = 0
    for i, (s, exp) in enumerate(tests, 1):
        res = count_substrings(s)
        ok = res == exp
        passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  s={s!r} -> got {res}, expected {exp}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()