class Stack:
    def __init__(self):
        self.size = 100
        self.top = -1
        self.arr = [None] * self.size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def stack_top(self):
        if not self.is_empty():
            return self.arr[self.top]
        else:
            return None

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
        else:
            self.top += 1
            self.arr[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return -1
        else:
            value = self.arr[self.top]
            self.top -= 1
            return value


def is_operator(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'


def precedence(ch):
    if ch == '*' or ch == '/':
        return 3
    elif ch == '+' or ch == '-':
        return 2
    else:
        return 0


def infix_to_postfix(infix):
    ptr = Stack()
    postfix = []
    i = 0  # Scanning infix
    j = 0  # Scanning and appending to postfix

    while i < len(infix):
        if not is_operator(infix[i]):
            postfix.append(infix[i])
            i += 1
            j += 1
        else:
            if precedence(infix[i]) > precedence(ptr.stack_top()):
                ptr.push(infix[i])
                i += 1
            else:
                postfix.append(ptr.pop())
                j += 1

    while not ptr.is_empty():
        postfix.append(ptr.pop())
        j += 1

    return ''.join(postfix)


# Example usage:
infix = "a + b * c - (d / e + f) * g"
print("Infix to postfix:", infix_to_postfix(infix))
