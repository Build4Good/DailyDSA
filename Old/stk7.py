tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Expected Output: 22

stack = []

for token in tokens:
    if token not in "+-*/":
        n=int(token)
        stack.append(n)

    
    else:
        # It's an operator.
        # 1. Pop the top two numbers.
        # 2. Perform the operation.
        # 3. Push the result back.
        b= stack[-1]
        stack.pop()
        a=stack[-1]
        stack.pop()
        if token=="+":
            c=a+b
            stack.append(int(c))
        elif token=="/":
            c=a/b
            stack.append(int(c))
        elif token=="*":
            c=a*b
            stack.append(int(c))
        else:
            c=a-b
            stack.append(int(c))  


print(stack[0])