temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
res = [0] * len(temperatures)
stk = [] # The Waiting List (indices)

for i,t in enumerate(temperatures):
    while stk and t>temperatures[stk[-1]]:
        previous_index=stk.pop()
        res[previous_index]=i-previous_index

    stk.append(i)

print(res)        
    