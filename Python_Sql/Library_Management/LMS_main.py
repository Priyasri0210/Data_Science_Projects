
from Library_management import *

#Display the menu options

def display_menu():
    print("==============Library Management System=================")
    print("Enter the option number only")
    print("1. Add book")
    print("2. Search book by ISBN_no")
    print("3. Update book details")
    print("4. Delete book")
    print("5. View books")
    print("6. checkout book")
    print("7. Return book")
    print("8. Exit")


def main():
    book_db = load_data() 

    while True:
        display_menu()
        choice = int(input("Enter your choice : "))

        if choice == 1:
            add_book(book_db)
        elif choice == 2:
            search_book(book_db)
        elif choice == 3:
            update_book(book_db)
        elif choice == 4:
            delete_book(book_db)
        elif choice == 5:
            view_books(book_db)
        elif choice == 6:
            check_out_book(book_db)
        elif choice == 7:
            return_book(book_db)    
        elif choice == 8:
            break
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()