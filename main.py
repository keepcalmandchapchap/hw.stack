from stack import Stack

def check_balance_of_string(string):
    stack = Stack()
    check = True

    for i in string:
        if i in '([{':
            stack.push(i)
        elif i in ')]}' and stack.is_empty():
            check = False

        if i == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                check = False
        elif i == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                check = False    
        elif i == '}':
            if stack.peek() == '{':
                stack.pop()
            else:
                check = False   
        
    if stack.is_empty() and check:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
    

