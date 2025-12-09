class Book:
    def __init__(self, title, author):
     self.title = title
     self.author = author

    def __str__(self):
       return f"{self.title} by {self.author}"
    
Book = Book("1984", "George Orwell")
print(Book) # 1984 by George Orwell