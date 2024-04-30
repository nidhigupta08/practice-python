# hash_map.py

class HashMap:
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        self.map[key] = value

    def search(self, key):
        return self.map.get(key, None)

    def delete(self, key):
        if key in self.map:
            del self.map[key]


# Example usage:
if __name__ == "__main__":
    hm = HashMap()
    hm.insert("apple", 10)
    hm.insert("banana", 20)
    hm.insert("cherry", 30)

    print("Value for key 'apple':", hm.search("apple"))  # 10
    print("Value for key 'banana':", hm.search("banana"))  # 20
    print("Value for key 'cherry':", hm.search("cherry"))  # 30

    hm.delete("banana")
    print("Value for key 'banana' after deletion:", hm.search("banana"))  # None
