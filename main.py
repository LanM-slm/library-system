from services.library_service import Library
from utils.json_utils import open_book, open_user
from models.book import Book
from models.member import User
from services.loan_service import first, second, third, fourth, fifth, sixth, seventh

def main():
    library = Library()
    books = open_book()
    users = open_user()
    print('IMPORTANT: To exit the library system, press Ctrl+C')
    print('1)Add new book')
    print('2)Display all available books')
    print('3)Borow book')
    print('4)Return book')
    print('5)Search_book')
    print('6)Tracking library statistics')
    print('7)Register')
    while True:
        try:
            user_answer = int(input('Enter a variant: '))
            if user_answer == 1:
                first(library, books)
            elif user_answer == 2:
                second(library, books)
            elif user_answer == 3:
                third(library, users, books)
            elif user_answer == 4:
                fourth(library, users, books)
            elif user_answer == 5:
                fifth(library, books)
            elif user_answer == 6:
                sixth(library)
            elif user_answer == 7:
                seventh(library, users)
        except ValueError:
            print('Invalid input!')
            continue
        except KeyboardInterrupt:
            print('\nBye, bye!')
            exit()
        
main()