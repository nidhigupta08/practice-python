# hash_table.py

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False


# Example usage:
if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("cherry", 30)

    print("Value for key 'apple':", ht.search("apple"))  # 10
    print("Value for key 'banana':", ht.search("banana"))  # 20
    print("Value for key 'cherry':", ht.search("cherry"))  # 30

    ht.delete("banana")
    print("Value for key 'banana' after deletion:", ht.search("banana"))  # None
