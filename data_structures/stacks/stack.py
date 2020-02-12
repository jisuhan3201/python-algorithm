class Stack:

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)
    
    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack.")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        

class StackOverflowError(BaseException):
    pass

if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    
    print("Stack demonstration:")
    print("Initial Stack : " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))

