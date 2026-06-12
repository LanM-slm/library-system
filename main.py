from classes import Book, Library
from classes import OpenBook, WriteBook
from classes import OpenUser, WriteUser
from classes import BookStatus

def first(library, books, write_book):
    book_name = input('Enter book name: ').title()
    author_name = input('Enter author name: ').title()
    flag, obj = library.find_book(book_name, author_name, books)
    if flag:
        print('That book exists!')
    else:
        obj_book = Book(book_name, author_name)
        books_write = library.add_book(obj_book.to_dict(), books)
        write_book.write(books_write)
        print('Book is added!')

def second(library, books):
    library.display_book(books)

def third(library, users, books, write_user, write_book):
    user_name = input('Enter your name: ').title().strip()
    flag, obj = library.find_name(user_name, users)
    if not flag:
        print('To borrow book, first register!')
    elif flag:
        book_name = input('Enter book name: ').title().lstrip().rstrip()
        author_name = input('Enter author name: ').title().lstrip().rstrip()
        flag2, obj2 = library.find_book(book_name, author_name, books)
        if flag2:
            if obj2.status == BookStatus.AVAILABLE.value:
                library.borrow_book(obj, obj2)
                idx_u = library.find_indexU(users, user_name)
                users[idx_u] = obj.to_dict()
                idx_b = library.find_indexB(books, book_name, author_name)
                books[idx_b] = obj2.to_dict()
                write_book.write(books)
                write_user.write(users)
                print('Book successfully borrowed!')
            else:
                print('Sorry, that book is already borrowed!')
        else:
            print('Sorry, that book is absent!')

def fourth(library, users, books, write_user, write_book):
    user_name = input('Enter your name: ').title().lstrip().rstrip()
    flag, obj = library.find_name(user_name, users)
    if not flag:
        print('Your name is not exist in users list!Please first register!')
    else:
        book_name = input('Enter book name: ').title().rstrip().lstrip()
        author_name = input('Enter author name: ').title().lstrip().rstrip()
        flag2, obj2 = library.find_book(book_name, author_name, books)
        if not flag2:
            print('That book does not exist!')
        else:
            is_exists = library.search_user_books(obj, obj2)
            if not is_exists:
                print('That book is not in your book list!')
            else:
                library.return_book(obj, obj2)
                idx_u = library.find_indexU(users, user_name)
                users[idx_u] = obj.to_dict()
                idx_b = library.find_indexB(books, book_name, author_name)
                books[idx_b] = obj2.to_dict()
                write_user.write(users)
                write_book.write(books)
                print('Book succesfully returned!')
def seventh(library, users, write_user):
    user_name = input('Enter your name: ').title().rstrip().lstrip()
    obj, flag = library.find_name(user_name, open_user.open())
    if flag:
        print('You have a registration card!')
    else:
        users = library.register(open_user.open(), user_name)
        write_user.write(users)
        print('Succesfully registerder!')

def main():
    library = Library()
    books = OpenBook().open()
    write_book = WriteBook()
    users = OpenUser().open()
    write_user = WriteUser()
    print('1)Add new book')
    print('2)Display all available books')
    print('3)Borow book')
    print('4)Return book')
    print('5)Search_book')
    print('7)Register')
    user_answer = int(input('Enter a variant: '))
    if user_answer == 1:
        first(library, books, write_book)
    elif user_answer == 2:
        second(library, books)
    elif user_answer == 3:
        third(library, users, books, write_user, write_book)
    elif user_answer == 4:
        fourth(library, users, books, write_user, write_book)
    elif user_answer == 7:
        seventh(library, users, write_user)
        
main()

