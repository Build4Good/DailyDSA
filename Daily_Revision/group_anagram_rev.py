"""REVISION — LeetCode 49: Group Anagrams. Group strings that are anagrams of each other."""
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # TODO: from memory
    dict_key={}

    for word in strs:
        word_s="".join(sorted(word))
        dict_key.setdefault(word_s,[]).append(word)

    return list(dict_key.values())

def run_tests():
    norm = lambda g: sorted(tuple(sorted(x)) for x in g)
    tests = [(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
             ([""], [[""]]), (["a"], [["a"]]), ([], []),
             (["abc","bca","cab","xyz"], [["abc","bca","cab"],["xyz"]]),
             (["aab","aba","baa"], [["aab","aba","baa"]])]
    passed = 0
    for i, (s, exp) in enumerate(tests, 1):
        res = group_anagrams(list(s)); ok = norm(res or []) == norm(exp); passed += ok
        print(f"Test {i}: {'PASS' if ok else 'FAIL'}  {s} -> {res}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()