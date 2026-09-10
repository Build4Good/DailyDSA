input="(([(()]))"
stk=[]
stk_flag=True
dict_brackets={"(":")","{":"}","[":"]"}
for bracket in input:
    if bracket=="(" or bracket=="[" or bracket=="{":
        stk.append(bracket)

    else:
        if (bracket==")" or bracket=="]" or bracket=="}") and len(stk)==0:
            stk_flag=False
        else:
            if (bracket==dict_brackets[stk[-1]]):
                stk.pop()
            else:
                stk_flag=False    

print(stk_flag and len(stk) == 0)


##Gemini SOlution ## 
input_str = "(([(()]))" # Renamed to avoid shadowing built-in 'input'
stk = []
valid = True
# Map Closing -> Opening (easier lookups)
lookup = {")": "(", "}": "{", "]": "["}

for char in input_str:
    if char in lookup: # It is a closing bracket
        # 1. Stack is empty? (Invalid) OR
        # 2. Top of stack doesn't match? (Invalid)
        if not stk or stk[-1] != lookup[char]:
            valid = False
            break
        stk.pop()
    else:
        # It is an opening bracket
        stk.append(char)

# FINAL CHECK: valid AND stack must be empty
print(valid and len(stk) == 0)