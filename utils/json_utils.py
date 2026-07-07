import json

def write(books):
    try:
        with open('books.json', 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Book file does not exist!')
        exit()

def open():
    try:
        with open('user.json', 'r', encoding='utf-8') as f:
            reader = json.load(f)
            return reader
    except FileNotFoundError:
        print('Users file does not exist!')
        exit()

def write(user):
    try:
        with open('user.json', 'w', encoding='utf-8') as f:
            json.dump(user, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print('Users file does not exist!')
        exit()  

def open():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            reader = json.load(f)
            return reader
    except FileNotFoundError:
        print('Books file does not exist!')
        exit()