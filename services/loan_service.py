def to_obj_book(to_obj, book_name, author_name, books, write_book, obj2):
    idx_b = to_obj.find_indexB(books, book_name, author_name)
    books[idx_b] = obj2.to_dict()
    write_book.write(books)

def to_obj_user(to_obj, users, user_name, write_user, obj):
    idx_u = to_obj.find_indexU(users, user_name)
    users[idx_u] = obj.to_dict()
    write_user.write(users)

def ask_for_register(library, users, write_user):
    while True:
        try:
            register = input('Do you want to register(y/n)? ').lower().strip()
            if register == 'y':
                seventh(library, users, write_user)
                break
            elif register == 'n':
                break
            else:
                print('Invalid input!')
                continue
        except KeyboardInterrupt:
            print('Bye, bye!')
            exit()

def first(library, books, write_book):
    try:
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
    except KeyboardInterrupt:
        print('Bye, bye!')
        exit()

def second(library, books):
    library.display_book(books)

def third(library, users, books, write_user, write_book, to_obj):
    try:
        user_name = input('Enter your name: ').title().strip()
        flag, obj = library.find_name(user_name, users)
        if not flag:
            print('To borrow book, first register!')
            ask_for_register(library, users, write_user)
        elif flag:
            book_name = input('Enter book name: ').title().lstrip().rstrip()
            author_name = input('Enter author name: ').title().lstrip().rstrip()
            flag2, obj2 = library.find_book(book_name, author_name, books)
            if flag2:
                if obj2.status == BookStatus.AVAILABLE.value:
                    library.borrow_book(obj, obj2)
                    to_obj_user(to_obj, users, user_name, write_user, obj)
                    to_obj_book(to_obj, book_name, author_name, books, write_book, obj2)
                    print('Book successfully borrowed!')
                else:
                    print('Sorry, that book is already borrowed!')
            else:
                print('Sorry, that book is absent!')
    except KeyboardInterrupt:
        print('Bye, bye!')
        exit()

def fourth(library, users, books, write_user, write_book, to_obj):
    try:
        user_name = input('Enter your name: ').title().lstrip().rstrip()
        flag, obj = library.find_name(user_name, users)
        if not flag:
            print('Your name does not exist in users list!Please first register!')
            ask_for_register(library, users, write_user)
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
                    print('Book succesfully returned!')
                    to_obj_user(to_obj, users, user_name, write_user, obj)
                    to_obj_book(to_obj, book_name, author_name, books, write_book, obj2)
    except KeyboardInterrupt:
        print('Bye, bye!')
        exit()

def fifth(library, books):
    while True:
        try:
            search = input('Search by book name or author name(b/a)? ').lower().strip()
            if search == 'b':
                book_name = input('Enter book name: ').title().rstrip().lstrip()
                print(library.search_book(books, book_name))
                break
            elif search == 'a':
                author_name = input('Enter author name: ').title().rstrip().lstrip()
                print(library.search_author(books, author_name))
                break
            else:
                print('Invalid input!')
                continue
        except KeyboardInterrupt:
            print('Bye, bye!')
            exit()
        
def sixth(library):
    print('Today trackers!')
    print('=' * 20)
    print(f'Registers: {library.registers}\nBorrows: {library.borrows}\nReturns: {library.returns}\nAdds: {library.adds}')

def seventh(library, users, write_user):
    try:
        user_name = input('Enter your name: ').title().rstrip().lstrip()
        obj, flag = library.find_name(user_name, users)
        if flag:
            print('You have a registration card!')
        else:
            users = library.register(users, user_name)
            write_user.write(users)
            print('Succesfully registerder!')
    except KeyboardInterrupt:
        print('Bye, bye!')
        exit()

