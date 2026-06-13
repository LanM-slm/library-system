from enum import Enum
import json
import random

#Book status class
class BookStatus(Enum):
    AVAILABLE = 'available'
    ISSUED = 'issued'

#Update book data
class WriteBook:
    @staticmethod
    def write(books):
        try:
            with open('books.json', 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4)
        except FileNotFoundError:
            print('Book file does not exist!')
            exit()

#Load book data
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

#Load user data
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

#Update user data
class WriteUser:
    @staticmethod
    def write(user):
        try:
            with open('user.json', 'w', encoding='utf-8') as f:
                json.dump(user, f, indent=4)
        except FileNotFoundError:
            print('Users file does not exist!')
            exit()

#Book class
class Book:
    def __init__(self, name, author, status=BookStatus.AVAILABLE.value):
        self.name = name
        self.author = author
        self.status = status
    def to_dict(self):
        return {'name': self.name,
                'author': self.author,
                'status': self.status}

#User class
class User:
    def __init__(self, name, id=random.randint(1, 500), books=[]):
        self.name = name
        self.id = id
        self.books = books
    def to_dict(self):
        return self.__dict__

#Class for converting objects to dictionaries
class ToObject:
    @staticmethod
    #Find index of dict in the book list
    def find_indexB(books, book_name, author_name):
        for i, book in enumerate(books):
            if book['name'] == book_name and book['author'] == author_name:
                return i
    #Find index of dict in the user list
    @staticmethod
    def find_indexU(users, user_name):
        for i, user in enumerate(users):
            if user['name'] == user_name:
                return i
#Main class Library
class Library:
    def __init__(self):
        self.borrows = 0
        self.returns = 0
        self.adds = 0
        self.registers = 0
    @staticmethod
    #Search user in the user list
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
    #Search book in the book list
    def find_book(book_name, author_name, books):
        if books == []:
            return False, None
        for book in books:
            if book_name == book['name'] and author_name == book['author']:
                obj = Book(book['name'], book['author'], book['status'])
                return True, obj
        return False, None
    #Search book in the user list
    def search_user_books(self, user, book):
        if book.name in user.books:
            return True
        else: 
            return False
    #1)Add new book
    def add_book(self, obj, books):
        books.append(obj)
        self.adds += 1
        return books
    #2)Display books
    def display_book(self, books):
        for book in books:
            if book['status'] == BookStatus.AVAILABLE.value:
                print(book)
    #3)Borrow book
    def borrow_book(self, user, book):
        book.status = BookStatus.ISSUED.value
        user.books.append(book.name)
        self.borrows += 1
    #4)Return book
    def return_book(self, user, book):
        user.books.remove(book.name)
        book.status = BookStatus.AVAILABLE.value
        self.returns += 1
    #5)Search book by book name
    def search_book(self, books, book_name):
        book_list = []
        for book in books:
            if book['name'] == book_name:
                book_list.append(book)
        if book_list:
            return book_list
        return 'Book does not exist!'
    #5)Search book by author name
    def search_author(self, books, author_name):
        book_list = []
        for book in books:
            if book['author'] == author_name:
                book_list.append(book)
        if book_list:
            return book_list
        return 'There are currently no works by this author!'
    #7)Register user
    def register(self, users, name):
        obj = User(name)
        users.append(obj.to_dict())
        self.registers += 1
        return users
    
    
