import json

def write_book(books):
    try:
        with open('utils/data/books.json', 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Book file does not exist!')
        exit()

def open_user():
    try:
        with open('utils/data/user.json', 'r', encoding='utf-8') as f:
            reader = json.load(f)
            return reader
    except FileNotFoundError:
        print('Users file does not exist!')
        exit()

def write_user(user):
    try:
        with open('utils/data/user.json', 'w', encoding='utf-8') as f:
            json.dump(user, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Users file does not exist!')
        exit()  

def open_book():
    try:
        with open('utils/data/books.json', 'r', encoding='utf-8') as f:
            reader = json.load(f)
            return reader
    except FileNotFoundError:
        print('Books file does not exist!')
        exit()