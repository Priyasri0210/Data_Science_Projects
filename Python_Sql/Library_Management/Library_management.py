import json
#from collections import defaultdict
def load_data():
    with open('E:/Git/DS-problems/projects/project_library_v2/Library.json','r') as f:
        book_db = json.load(f)
        return book_db
        
def save_data(data):
    with open('E:/Git/DS-problems/projects/project_library_v2/Library.json','w') as f:
        json.dump(data,f)

def add_book(book_db,Borrowed=0):
    try:
        ISBN_no = (input("Enter ISBN_no: "))
        
        if ISBN_no in book_db:
            print('ISBN_no is already registered')
            return None
        
        Title = input("Enter Book title : ")
        Author= input('Enter Author name : ')
        Genre = input("Enter Book Genre : ")
        Copies = int(input('Enter no.of copies : '))
        
        book_db[ISBN_no] = {"Title":Title,"Author":Author,"Genre":Genre,"Copies":Copies,"Borrowed":Borrowed}
        save_data(book_db)
        print('Book registered successfully')
    except Exception as e:
        print('error in adding book')
        print(e)

def search_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be searched : ")
    if ISBN_no in book_db:
        print("Details : ")
        print(book_db[ISBN_no])
    else:
        print('Book is not available')

def update_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be updated : ")
    if ISBN_no not in book_db:
        print("Book is not available")
    else:
        print('Enter blank space if no changes needed')
        print(book_db[ISBN_no])
        new_title = input("Enter Book title : ")
        Title = new_title if new_title else book_db[ISBN_no]['Title']
        new_author= input('Enter Author name : ')
        Author = new_author if new_author else book_db[ISBN_no]['Author']
        new_genre = input("Enter Book Genre : ")
        Genre = new_genre if new_genre else book_db[ISBN_no]['Genre']
        new_copies = int(input('Enter no.of copies : '))
        Copies = new_copies if new_copies else book_db[ISBN_no]['Copies']
        new_borrowed = int(input("No. of copies borrowed: "))
        Borrowed = new_borrowed if new_borrowed else book_db[ISBN_no]['Borrowed']
        book_db[ISBN_no] = {"Title":Title,"Author":Author,"Genre":Genre,"Copies":Copies,"Borrowed":Borrowed}
        save_data(book_db)
        print('Book details updated successfully')

def delete_book(book_db):
    ISBN_no = input("Enter the ISBN_no to be deleted : ")
    if ISBN_no not in book_db:
        print("Book is not available")
    else:
        del book_db[ISBN_no]
        save_data(book_db)
        print('Book deleted successfully')

def view_books(book_db):
    if book_db:
        for ISBN, details in book_db.items():
            print("ISBN_no : {}, Title : {}, Author : {}, Genre : {}, Copies : {}, Borrowed : {}".format(ISBN,details['Title'],details['Author'],details['Genre'],details['Copies'],details['Borrowed']))
    else:
        print('No books in database')

def check_out_book(book_db):
    ISBN_no = input("Enter the ISBN_no of book to be borrow : ")
    if ISBN_no not in book_db:
        print("Book is not available")
        return
    elif book_db[ISBN_no]["Copies"] <= 0:
        print("No copies available for Borrowing")
        return
    elif ISBN_no in book_db and book_db[ISBN_no]["Copies"] > 0:
        user = input("Enter User ID or Name: ")
        book_db[ISBN_no]["Copies"] -= 1
        book_db[ISBN_no]["Borrowed"] += 1
        save_data(book_db)
        print("Book_no {} is checked out successfully by user {}" .format(ISBN_no, user))
        
    

def return_book(book_db):
    ISBN_no = input("Enter the ISBN_no of book to be return : ")
    if ISBN_no not in book_db:
        print("Book is not available")
        return
    elif ISBN_no in book_db:
        user = input("Enter user ID or name: ")
        book_db[ISBN_no]["Copies"] += 1
        book_db[ISBN_no]["Borrowed"] -= 1
        save_data(book_db)
        print("Book_no {} is returned successfully by user {}" .format(ISBN_no, user))
       
