class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

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
    print("Is the stack empty?", s.is_empty())  # True

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print("Is the stack empty?", s.is_empty())  # False
    print("Top of the stack:", s.peek())         # 4
    print("Stack size:", s.size())               # 4

    print("Popped item:", s.pop())               # 4
    print("Top of the stack after pop:", s.peek()) # 3
    print("Stack size after pop:", s.size())      # 3
