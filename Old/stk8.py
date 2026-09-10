temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
res = [0] * len(temperatures)  # Initialize result with 0s
stack = []  # Stores INDICES, not values

for i, t in enumerate(temperatures):
    
    while stack and t > temperatures[stack[-1]]:
        previous_index=stack[-1]
        res[previous_index]=i-previous_index
        stack.pop()
        
        
    
    stack.append(i)

print(res)