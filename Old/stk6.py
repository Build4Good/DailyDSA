s = "abbaca"
stk = []

for char in s:
    if stk and stk[-1]==char:
        stk.pop()
    else:
        stk.append(char)

print("".join(stk))