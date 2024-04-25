# linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    print("Is the linked list empty?", ll.is_empty())  # True

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Is the linked list empty?", ll.is_empty())  # False
    print("Linked list:", end=" ")
    ll.display()
