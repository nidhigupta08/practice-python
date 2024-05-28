class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title             # Public attribute
        self.director = director       # Public attribute
        self.year = year               # Public attribute
        self.__rating = rating         # Private attribute

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("Invalid rating! Rating should be between 0 and 10.")

    def display_movie_details(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")
        print(f"Rating: {self.get_rating()}")

# Creating a Movie object
movie = Movie("Inception", "Christopher Nolan", 2010, 8.8)

# Displaying movie details
movie.display_movie_details()
# Output:
# Title: Inception
# Director: Christopher Nolan
# Year: 2010
# Rating: 8.8

# Changing rating
movie.set_rating(9.0)
movie.display_movie_details()
# Output:
# Title: Inception
# Director: Christopher Nolan
# Year: 2010
# Rating: 9.0
