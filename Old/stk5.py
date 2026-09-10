def backSpaceCompare(s,t):

    def build(String):
        stk=[]
        for char in String:
            if char!="#":
                stk.append(char)
            else:
                stk.pop()

        return stk
    
    return ("".join(build(s))=="".join(build(t)))



s = "ab##c#"
t = "ab##d#"

print(backSpaceCompare(s,t))