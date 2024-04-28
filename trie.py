# trie.py

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage:
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print("Is 'apple' in trie?", trie.search("apple"))  # True
    print("Is 'app' in trie?", trie.search("app"))      # True
    print("Is 'banana' in trie?", trie.search("banana"))  # True
    print("Starts with 'ban'?", trie.starts_with("ban"))  # True
    print("Starts with 'bana'?", trie.starts_with("bana"))  # True
    print("Starts with 'banz'?", trie.starts_with("banz"))  # False
