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
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Is the stack empty?", s.is_empty())  # False
    print("Top of the stack:", s.peek())        # 3
    print("Stack size:", s.size())              # 3

    print("Popped item:", s.pop())              # 3
    print("Top of the stack after pop:", s.peek())  # 2
    print("Stack size after pop:", s.size())       # 2
