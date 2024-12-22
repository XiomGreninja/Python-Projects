class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}."
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books! The books are")
        for book in self.books:
            print(book)

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            self.noBooks = len(self.books)
        else:
            print("Book not found!")

    def searchBook(self, search_term):
        

    
l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Sapiens")
l1.showInfo()

    