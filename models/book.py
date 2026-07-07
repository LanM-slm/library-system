class Book:
    def __init__(self, name, author, status=BookStatus.AVAILABLE.value):
        self.name = name
        self.author = author
        self.status = status
    def to_dict(self):
        return {'name': self.name,
                'author': self.author,
                'status': self.status}
    def find_indexB(self, books, book_name, author_name):
        for i, book in enumerate(books):
            if book['name'] == book_name and book['author'] == author_name:
                return i