"""
LeetCode 20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets are closed by the same type of bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
    s = "()[]{}"  -> True
    s = "(]"       -> False
    s = "([)]"     -> False  (wrong ORDER, even though all brackets are present)
"""


def is_valid(s: str) -> bool:
    # TODO: implement your solution here
    stk=[]
    dict_par={"(":")","[":"]","{":"}"}
    
    for ch in s:
        if ch in dict_par.keys():
            stk.append(ch)
        else:
            if not stk or dict_par[stk[-1]] != ch:
                return False   # mismatch OR nothing to match against -- invalid immediately
            stk.pop()  

    return not(stk)


# ─────────────────────────────────────────────
# Test cases — run this file directly to check yourself
# ─────────────────────────────────────────────

def run_tests():
    tests = [
        ("()", True),                # simplest valid case
        ("()[]{}", True),             # multiple, all closed correctly
        ("(]", False),                 # mismatched types
        ("([)]", False),               # right brackets, WRONG order
        ("{[]}", True),                 # properly nested
        ("", True),                      # empty string -- vacuously valid
        ("(", False),                    # unclosed open bracket
        (")", False),                    # closing bracket with nothing open
        ("((()))", True),                 # deeply nested, same type
    ]

    passed = 0
    for i, (s, expected) in enumerate(tests, 1):
        result = is_valid(s)
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"Test {i}: {status}  s={s!r} -> got {result}, expected {expected}")

    print()
    print(f"{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()