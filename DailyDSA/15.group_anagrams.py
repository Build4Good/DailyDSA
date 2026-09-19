"""
LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example:
    strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    dict_grp={}

    for word in strs:
        sorted_word=sorted(word)
        sorted_word="".join(c for c in sorted_word)
        dict_grp.setdefault(sorted_word, []).append(word)
            

    return list(dict_grp.values())


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# (group order and order WITHIN each group don't matter)
# ─────────────────────────────────────────────

def normalize(groups):
    return sorted(tuple(sorted(g)) for g in groups)


def run_tests():
    tests = [
        (["eat","tea","tan","ate","nat","bat"],
         [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),                          # single empty string
        (["a"], [["a"]]),                          # single character
        (["abc","bca","cab","xyz"],
         [["abc","bca","cab"],["xyz"]]),            # one group of 3, one singleton
        ([], []),                                    # empty input list
        (["aab","aba","baa"],
         [["aab","aba","baa"]]),                     # duplicate-letter anagrams
    ]

    passed = 0
    for i, (strs, expected) in enumerate(tests, 1):
        result = group_anagrams(strs)
        result_norm = normalize(result) if result else []
        expected_norm = normalize(expected)
        ok = result_norm == expected_norm
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  strs={strs} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()