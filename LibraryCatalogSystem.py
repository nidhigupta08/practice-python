class LibraryItem:
    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"


class DVD(LibraryItem):
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def display_info(self):
        return f"DVD: {self.title} directed by {self.director}"


# Usage
book = Book("To Kill a Mockingbird", "Harper Lee")
print(book.display_info())

dvd = DVD("The Shawshank Redemption", "Frank Darabont")
print(dvd.display_info())
