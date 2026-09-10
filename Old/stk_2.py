class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)==0:
            self.min_stack.append(val)
        else:
            if not self.min_stack or val<=self.min_stack[-1]:
                self.min_stack.append(val)



    def pop(self) -> None:
        topvalue=self.stack[-1]
        del self.stack[-1]

        if topvalue==self.min_stack[-1]:
            del self.min_stack[-1]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    


min_stk=MinStack()
min_stk.push(5)
min_stk.push(6)
min_stk.push(3)
min_stk.push(7)
print(min_stk.top())
print(min_stk.getMin())
min_stk.pop()
min_stk.pop()
print(min_stk.top())
print(min_stk.getMin())


### Gemini Code ###
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # FIX: Check if empty OR val is less than OR EQUAL to current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Use .pop() - it's cleaner than del list[-1]
        val = self.stack.pop() 
        
        # If the value we just removed was the minimum, remove it from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]