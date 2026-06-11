from enum import Enum
import json
import random

class BookStatus(Enum):
    AVAILABLE = 'available'
    ISSUED = 'issued'

class WriteBook:
    @staticmethod
    def write(books):
        try:
            with open('books.json', 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4)
                return 'Book is added!'
        except FileNotFoundError:
            print('Book file does not exist!')
            exit()

class OpenBook:
    @staticmethod
    def open():
        try:
            with open('books.json', 'r', encoding='utf-8') as f:
                reader = json.load(f)
                return reader
        except FileNotFoundError:
            print('Book file does not exist!')
            exit()

class OpenUser:
    @staticmethod
    def open():
        try:
            with open('user.json', 'r', encoding='utf-8') as f:
                reader = json.load(f)
                return reader
        except FileNotFoundError:
            print('Users file does not exist!')
            exit()

class WriteUser:
    @staticmethod
    def write(user):
        try:
            with open('user.json', 'w', encoding='utf-8') as f:
                json.dump(user, f, indent=4)
        except FileNotFoundError:
            print('Users file does not exist!')
            exit()

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.status = BookStatus.AVAILABLE
    def to_dict(self):
        return {'name': self.name,
                'author': self.author}

class Library:
    users_list = []
    books_list = []

    def add_book(self, books, book):
        books.append(book.to_dict())
        return books
    def display_book(self, books):
        for book in books:
            obj = Book(book['name'], book['author'])
            if obj.status == BookStatus.AVAILABLE:
                print(book)
    @staticmethod
    def find_name(name, users):
        for user in users:
            for v in user.values():
                if v == name:
                    obj = User(user['name'])
                    return True, obj
        return False, None
    @staticmethod
    def find_book(book_name, author_name, books):
        for book in books:
            if book_name in book.values() and author_name in book.values():
                obj = Book(book['name'], book['author'])
                return True, obj
        return False, None
    def borrow_book(self, user, book, users):
        book.status = BookStatus.ISSUED
        user.books.append(book.name)
        users.append(user.to_dict())
        return users
    def register(self, users, name):
        obj = User(name)
        users.append(obj.to_dict())
        return users

class User:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1, 500)
        self.books = []
    def to_dict(self):
        return self.__dict__
    
