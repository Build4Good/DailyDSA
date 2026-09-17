"""
LeetCode 424: Longest Repeating Character Replacement


You are given a string s and an integer k. You can choose any
character of the string and change it to any other uppercase English
character, up to k times.

Return the length of the longest substring containing the same
letter you can get after performing the above operations.

Example:
    s = "ABAB", k = 2
    Output: 4  (replace the two 'A's with 'B's, or vice versa)

    s = "AABABBA", k = 1
    Output: 4  ("ABBA" -> replace the middle 'A' to make "BBBB",
                or "AABA" -> replace one to get "AAAA")
"""


def character_replacement(s: str, k: int) -> int:
    count={}
    res=0
    max_frq=0
    l=0

    for r in range(len(s)):
        count[s[r]]=count.get(s[r],0)+1
        max_frq=max(max_frq,count[s[r]])

        while (r-l+1)-max_frq>k:
            count[s[l]]-=1
            l+=1
        res=max(res,r-l+1)

    return res        


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("ABAB", 2, 4),           # classic case
        ("AABABBA", 1, 4),         # window isn't at the start or end
        ("AAAA", 2, 4),            # already all the same, k unused
        ("A", 0, 1),               # single character, no replacements allowed
        ("ABCDE", 1, 2),           # all distinct, k only helps a little
        ("ABBB", 2, 4),            # k more than enough
        ("", 0, 0),                # empty string
        ("AAAB", 0, 3),            # k=0 -- no replacements allowed at all
    ]

    passed = 0
    for i, (s, k, expected) in enumerate(tests, 1):
        result = character_replacement(s, k)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r}, k={k} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()