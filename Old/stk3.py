tokens = ["4", "13", "5", "/", "+"]
stk=[]

for token in tokens:
    if token not in "+-*/":
        stk.append(int(token))
    else:
        a=stk[-1]
        del stk[-1]
        b=stk[-1]
        del stk[-1]
        if token == "+":
            stk.append(int(b) + int(a))
        elif token == "-":
            stk.append(int(b) - int(a))  # Order matters: left - right
        elif token == "*":
            stk.append(int(b) * int(a))
        elif token == "/":
            stk.append(int(int(b)/int(a)))   

print(stk)            