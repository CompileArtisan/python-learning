def main():
    stk = Stack()
    for i in range(5):
        stk.push(i * 10)

    stk.printStack()
        
        
class Stack:
    def __init__(self):
        self.stack = []
        self.TOP = -1

    def push(self, value):
        self.TOP += 1
        if len(self.stack) > self.TOP:
            self.stack[self.TOP] = value
        else:
            self.stack.append(value)

    def pop(self):
        if self.TOP == -1:
            return None
        value = self.stack[self.TOP]
        self.TOP -= 1
        return value

    def peek(self):
        if self.TOP == -1:
            return None
        return self.stack[self.TOP]
    
    def printStack(self):
        for i in range(self.TOP, -1, -1):
            print(self.stack[i])



if __name__ == "__main__":
    main()