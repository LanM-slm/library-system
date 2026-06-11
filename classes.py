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
    def __init__(self, name, author, status=BookStatus.AVAILABLE.value):
        self.name = name
        self.author = author
        self.status = status
    def to_dict(self):
        return {'name': self.name,
                'author': self.author,
                'status': BookStatus.AVAILABLE.value}

class Library:
    def add_book(self, obj, books):
        books.append(obj)
        return books
    def display_book(self, books):
        for book in books:
            if book['status'] == BookStatus.AVAILABLE.value:
                print(book)
    @staticmethod
    def find_name(name, users):
        if users == []:
            return False, None
        for user in users:
            for v in user.values():
                if v == name:
                    obj = User(user['name'], user['id'], user['books'])
                    return True, obj
        return False, None
    @staticmethod
    def find_book(book_name, author_name, books):
        if books == []:
            return False, None
        for book in books:
            if book_name in book.values() and author_name in book.values():
                obj = Book(book['name'], book['author'], book['status'])
                return True, obj
        return False, None
    def borrow_book(self, user, book):
        book.status = BookStatus.ISSUED.value
        user.books.append(book.name)
    def register(self, users, name):
        obj = User(name)
        users.append(obj.to_dict())
        return users

class User:
    def __init__(self, name, id=random.randint(1, 500), books=[]):
        self.name = name
        self.id = id
        self.books = books
    def to_dict(self):
        return self.__dict__
    
