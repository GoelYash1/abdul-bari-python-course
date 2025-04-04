class Book:
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

book1 = Book("Harry Potter", "JK Rowling",350)
book2 = Book("Lord of the Rings", "J.R.R. Tolkein",450)

book1.show_details()
book2.show_details()