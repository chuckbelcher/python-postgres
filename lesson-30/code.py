class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book {self.name}, {self.book_type}, {self.weight}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def softcover(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight + 10)


myhardbook = Book.hardcover("Harry Potter", 34)
mysoftbook = Book.softcover("Philip the dog", 14)
print(myhardbook)
print(mysoftbook)