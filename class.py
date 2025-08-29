
# Parent class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.__rating = None  # Encapsulation (private attribute)

    def set_rating(self, rating):
        """Set book rating safely (0-5)."""
        if 0 <= rating <= 5:
            self.__rating = rating
        else:
            print("Rating must be between 0 and 5.")

    def get_rating(self):
        """Get book rating."""
        return self.__rating

    def get_summary(self):
        return f"'{self.title}' by {self.author}, published in {self.year}."


# Child class (Inheritance + Polymorphism)
class Novel(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    # Method overriding (Polymorphism)
    def get_summary(self):
        return f"Novel: '{self.title}' ({self.genre}) by {self.author}, published in {self.year}."


# Another Child class
class Textbook(Book):
    def __init__(self, title, author, year, subject):
        super().__init__(title, author, year)
        self.subject = subject

    # Method overriding (Polymorphism)
    def get_summary(self):
        return f"Textbook: '{self.title}' on {self.subject}, by {self.author} ({self.year})."


# Create objects
book1 = Novel("Things Fall Apart", "Chinua Achebe", 1958, "Historical Fiction")
book2 = Novel("Purple Hibiscus", "Chimamanda Ngozi Adichie", 2003, "Coming-of-age")
book3 = Textbook("The Last Days at Forcados High School", "A.H. Mohammed", 2013, "Literature")

# Encapsulation: setting ratings
book1.set_rating(5)
book2.set_rating(4)
book3.set_rating(3)

# Print summaries (Polymorphism in action)
print(book1.get_summary())
print("Rating:", book1.get_rating())
print()

print(book2.get_summary())
print("Rating:", book2.get_rating())
print()

print(book3.get_summary())
print("Rating:", book3.get_rating())


    