class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title         # Public attribute
        self.author = author       # Public attribute
        self.isbn = isbn           # Public attribute
        self.__copies = copies     # Private attribute

    def get_copies(self):
        return self.__copies

    def add_copies(self, count):
        if count > 0:
            self.__copies += count
        else:
            print("Invalid number of copies to add!")

    def remove_copies(self, count):
        if 0 < count <= self.__copies:
            self.__copies -= count
        else:
            print("Invalid number of copies to remove!")

    def display_book_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Copies Available: {self.get_copies()}")

# Creating a Book object
book = Book("1984", "George Orwell", "9780451524935", 10)

# Displaying book details
book.display_book_details()
# Output:
# Title: 1984
# Author: George Orwell
# ISBN: 9780451524935
# Copies Available: 10

# Adding copies
book.add_copies(5)
book.display_book_details()
# Output:
# Title: 1984
# Author: George Orwell
# ISBN: 9780451524935
# Copies Available: 15

# Removing copies
book.remove_copies(3)
book.display_book_details()
# Output:
# Title: 1984
# Author: George Orwell
# ISBN: 9780451524935
# Copies Available: 12
