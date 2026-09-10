temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
res = [0] * len(temperatures)
stk = [] # The Waiting List (indices)

for i, t in enumerate(temperatures):
    # While list has people AND current temp t > temp of person at top of list
    while stk and t > temperatures[stk[-1]]:
        prev_index = stk.pop()
        res[prev_index] = i - prev_index
    
    stk.append(i)

print(res)