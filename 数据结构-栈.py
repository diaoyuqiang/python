class Stack():
    def __init__(self):
        self.stack = []
    def push(self, element): # 入栈、压栈
        self.stack.append(element)
    def pop(self): # 取栈
        return self.stack.pop()
    def get_top(self): # 取栈顶
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return  None
    def is_empty(self):
        return len(self.stack) == 0

# 括号匹配问题

def brace_match(s):
    match = {'}': '{', ']': '[', ')': '('}
    stack =Stack()
    for ch in s:
        if ch in {'(', '[', '{'}: # 左括号入栈
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop() # 右括号匹配出栈
            else:
                return False # 不匹配false

    if stack.is_empty():
        return True
    else:
        return False


print(brace_match('()[]{}'))