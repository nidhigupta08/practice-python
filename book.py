class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def turn_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"Page {self.current_page} of {self.pages}")
        else:
            print("You've reached the end of the book.")

# Creating an instance of the Book class
my_book = Book("Python for Beginners", "John Smith", 200)

# Accessing attributes and methods of the Book instance
print(my_book.info())
my_book.turn_page()
my_book.turn_page()
my_book.turn_page()
