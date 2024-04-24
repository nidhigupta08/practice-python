# queue.py

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    q = Queue()
    print("Is the queue empty?", q.is_empty())  # True

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Is the queue empty?", q.is_empty())  # False
    print("Front of the queue:", q.peek())         # 1
    print("Queue size:", q.size())               # 4

    print("Dequeued item:", q.dequeue())               # 1
    print("Front of the queue after dequeue:", q.peek()) # 2
    print("Queue size after dequeue:", q.size())      # 3
