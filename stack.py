class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def push(self, foo):
        self.stack.append(foo)

    def pop(self):
        removed_value = self.stack.pop()
        return removed_value
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True
        
    