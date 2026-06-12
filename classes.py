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
                'status': self.status}

class Library:
    def __init__(self):
        self.borrows = 0
        self.returns = 0
        self.adds = 0
        self.registers = 0
    def add_book(self, obj, books):
        books.append(obj)
        self.adds += 1
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
            if book_name == book['name'] and author_name == book['author']:
                obj = Book(book['name'], book['author'], book['status'])
                return True, obj
        return False, None
    def borrow_book(self, user, book):
        book.status = BookStatus.ISSUED.value
        user.books.append(book.name)
        self.borrows += 1
    def register(self, users, name):
        obj = User(name)
        users.append(obj.to_dict())
        self.registers += 1
        return users
    def find_indexB(self, books, book_name, author_name):
        for i, book in enumerate(books):
            if book['name'] == book_name and book['author'] == author_name:
                return i
    def find_indexU(self, users, user_name):
        for i, user in enumerate(users):
            if user['name'] == user_name:
                return i
    def search_user_books(self, user, book):
        if book.name in user.books:
            return True
        else: 
            return False
    def return_book(self, user, book):
        user.books.remove(book.name)
        book.status = BookStatus.AVAILABLE.value
        self.returns += 1
    def search_book(self, books, book_name):
        book_list = []
        for book in books:
            if book['name'] == book_name:
                book_list.append(book)
        if book_list:
            return book_list
        return 'Book does not exist!'
    def search_author(self, books, author_name):
        book_list = []
        for book in books:
            if book['author'] == author_name:
                book_list.append(book)
        if book_list:
            return book_list
        return 'There are currently no works by this author!'
class User:
    def __init__(self, name, id=random.randint(1, 500), books=[]):
        self.name = name
        self.id = id
        self.books = books
    def to_dict(self):
        return self.__dict__
    
