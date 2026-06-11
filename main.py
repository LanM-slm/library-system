from classes import Book, Library
from classes import OpenBook, WriteBook
from classes import OpenUser, WriteUser
from classes import BookStatus

def first(library, open_book, write_book):
    book_name = input('Enter book name: ').title()
    author_name = input('Enter author name: ').title()
    book = Book(book_name, author_name)
    print(write_book.write(library.add_book(open_book.open(), book)))

def second(library, open_book):
    library.display_book(open_book.open())

def third(library, open_user, open_book, write_user):
    user_name = input('Enter your name: ').title().strip()
    flag, obj = library.find_name(user_name, open_user.open())
    if not flag:
        print('To borrow book, first register!')
    elif flag:
        book_name = input('Enter book name: ').title().lstrip().rstrip()
        author_name = input('Enter author name: ').title().lstrip().rstrip()
        flag2, obj2 = library.find_book(book_name, author_name, open_book.open())
        if flag2:
            if obj2.status == BookStatus.AVAILABLE:
                user_obj = library.borrow_book(obj, obj2, open_user.open())
                print('Book successfully borrowed!')
            else:
                print('Sorry, that book is already borrowed!')
        else:
            print('Sorry, that book is absent!')

def seventh(library, open_user, write_user):
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
    open_book = OpenBook()
    write_book = WriteBook()
    open_user = OpenUser()
    write_user = WriteUser()
    print('1)Add new book')
    print('2)Display all available books')
    print('3)Borow book')
    print('7)Register')
    user_answer = int(input('Enter a variant: '))
    if user_answer == 1:
        first(library, open_book, write_book)
    elif user_answer == 2:
        second(library, open_book)
    elif user_answer == 3:
        third(library, open_user, open_book, write_user)
    elif user_answer == 7:
        seventh(library, open_user, write_user)
        
       

main()
