class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None


def parenthesis_checker(exp):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in exp:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if opening_brackets.index(top_char) != closing_brackets.index(char):
                return False

    return stack.is_empty()


# Example usage:
exp1 = "[(2+3)+{4}]"
exp2 = "{[(2+3)*4]+5}"
exp3 = "[((2+3)*4]+5)"

print("Expression 1:", "Balanced" if parenthesis_checker(exp1) else "Unbalanced")
print("Expression 2:", "Balanced" if parenthesis_checker(exp2) else "Unbalanced")
print("Expression 3:", "Balanced" if parenthesis_checker(exp3) else "Unbalanced")
