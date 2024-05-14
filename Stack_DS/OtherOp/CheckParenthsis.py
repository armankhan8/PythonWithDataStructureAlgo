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

    for char in exp:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


# Example usage:
exp1 = "(2+3)*(4-1)"
exp2 = "((2+3)*4"
exp3 = ")(2+3)*4"
exp4 = "((2+3)*4)"

print("Expression 1:", "Balanced" if parenthesis_checker(exp1) else "Unbalanced")
print("Expression 2:", "Balanced" if parenthesis_checker(exp2) else "Unbalanced")
print("Expression 3:", "Balanced" if parenthesis_checker(exp3) else "Unbalanced")
print("Expression 4:", "Balanced" if parenthesis_checker(exp4) else "Unbalanced")
